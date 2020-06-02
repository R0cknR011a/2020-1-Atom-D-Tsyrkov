import time
import asyncio
import aiohttp


def write_file(data):
    name = f'photo_{int(time.time() * 1000)}'
    with open(name, 'wb') as f:
        f.write(data)


async def writer(to_output):
    count = 0
    loop = asyncio.get_running_loop()
    while count < 10:
        data = await to_output.get()
        await loop.run_in_executor(None, write_file, data)
        to_output.task_done()
        count += 1


async def fetch(url, session, to_output):
    async with session.get(url, allow_redirects=True) as resp:
        data = await resp.read()
        to_output.put_nowait(data)


async def main():
    url = 'https://loremflickr.com/320/240'
    tasks = []
    to_output = asyncio.Queue()
    async with aiohttp.ClientSession() as session:
        for i in range(10):
            tasks.append(fetch(url, session, to_output))

        await asyncio.gather(*(tasks + [writer(to_output)]))


if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()

    print('TT', t2 - t1)
