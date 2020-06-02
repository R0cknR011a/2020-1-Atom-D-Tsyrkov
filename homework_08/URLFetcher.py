import asyncio
import aiohttp


class Fetcher:
    def __init__(self, n_workers, input_file_name, output_file_name, FORMAT='utf-8'):
        self.n_workers = n_workers
        self.output_file_name = output_file_name
        self.input_file_name = input_file_name
        self.FORMAT = FORMAT
        self.urls = []
        self.task_count = 0
        with open(input_file_name, 'r') as f:
            for line in f:
                self.urls.append(line.strip())
                self.task_count += 1

    async def main(self):
        self.loop = asyncio.get_running_loop()
        self.to_output = asyncio.Queue()
        self.tasks = asyncio.Queue()
        for url in self.urls:
            self.tasks.put_nowait(url)

        async with aiohttp.ClientSession() as session:
            workers = []
            for i in range(self.n_workers):
                workers.append(self.worker(i, session))

            await asyncio.gather(*(workers + [self.file_writer()]), return_exceptions=True)

        await self.tasks.join()
        await self.to_output.join()

    async def worker(self, worker_id, session):
        while not self.tasks.empty():
            url = await self.tasks.get()
            async with session.get(url, allow_redirects=True) as resp:
                data = await resp.read()
                data = data.decode(self.FORMAT)
                self.to_output.put_nowait(data)
                print(f'[WORKER #{worker_id}] {url}')
                self.tasks.task_done()

    async def file_writer(self):
        output_count = 0
        while output_count != self.task_count:
            data = await self.to_output.get()
            await self.loop.run_in_executor(None, self.write_file, data)
            self.to_output.task_done()
            output_count += 1

    def write_file(self, data):
        with open(self.output_file_name, 'a') as f:
            f.write(data)
            f.write('\n' + '-' * 200 + '\n')

    def start(self):
        asyncio.run(self.main(), debug=True)
