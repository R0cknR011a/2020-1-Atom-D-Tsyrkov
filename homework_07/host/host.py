import socket
import requests
from bs4 import BeautifulSoup
import threading, queue
from sys import getsizeof as size


class MasterWorker:
    def __init__(self, n_workers, BUFFER_SIZE):
        self.workers = []
        self.users = []
        self.connections = []
        self.n_workers = n_workers
        self.tasks = queue.Queue()
        self.tasks_done = queue.Queue()
        self.tasks_count = [0] * n_workers
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.message_length = BUFFER_SIZE - 33

    def terminate(self, signal_num, frame):
        self.working_status = False
        self.user_connect.join()
        for user in self.users:
            user.join()
        for worker in self.workers:
            worker.join()
        self.user_output.join()
        for connection in self.connections:
            connection.close()
        self.sock.close()
        tasks_done = [x for x in self.tasks_count]
        print(f'[TERMINATE] Tasks done: {tasks_done}, Total: {sum(tasks_done)}\nTERMINATED SUCCESSFULLY')

    def engage(self, host, connection_timeout=5, receive_timeout=5, FORMAT='utf-8'):
        self.working_status = True
        self.user_connect = threading.Thread(target=self.user_connect, args=(
                host, connection_timeout, receive_timeout, FORMAT,
            ))
        self.user_output = threading.Thread(target=self.user_output, args=(FORMAT,))
        self.user_connect.start()
        for i in range(self.n_workers):
            worker = threading.Thread(target=self.handle_url, args=(i, FORMAT,))
            self.workers.append(worker)
            worker.start()
        self.user_output.start()

    def handle_url(self, worker_id, FORMAT):
        print(f'[WORKER #{worker_id}] Engaged')
        while self.working_status:
            if not self.tasks.empty():
                try:
                    connection, data = self.tasks.get(timeout=3)
                except queue.Empty:
                    continue
                response = requests.get(data).text
                soup = BeautifulSoup(response, features='html.parser')
                for script in soup(['script', 'style']):
                    script.extract()
                text = soup.get_text()
                text = '\n'.join(item for item in text.split('\n') if item)
                self.tasks_done.put((connection, text))
                self.tasks.task_done()
                self.tasks_count[worker_id] += 1
        print(f'[WORKER #{worker_id}] Terminating')

    def user_input(self, connection, user_id, FORMAT):
        print(f'[USER #{user_id}] Engaged')
        while self.working_status:
            try:
                data = connection.recv(1024)
            except socket.timeout:
                continue
            else:
                if data:
                    data = data.decode(FORMAT)
                    self.tasks.put((connection, data))
                else:
                    break
        print(f'[USER #{user_id}] Terminating')

    def user_connect(self, host, connection_timeout, receive_timeout, FORMAT):
        print('[CONNECT] Engaged')
        self.sock.bind(host)
        self.sock.listen()
        self.sock.settimeout(connection_timeout)
        while self.working_status:
            try:
                connection, address = self.sock.accept()
            except socket.timeout:
                continue
            else:
                self.connections.append(connection)
                connection.settimeout(receive_timeout)
                user = threading.Thread(target=self.user_input, args=(
                         connection, len(self.users), FORMAT,
                    ))
                self.users.append(user)
                user.start()
        print('[CONNECT] Terminating')

    def user_output(self, FORMAT):
        print('[OUTPUT] Engaged')
        while self.working_status:
            if not self.tasks_done.empty():
                connection, text = self.tasks_done.get()
                text_size = str(size(text))
                while len(text_size) != self.message_length:
                    text_size += 'X'
                try:
                    connection.send(text_size.encode(FORMAT))
                    connection.send(text.encode(FORMAT))
                except BrokenPipeError:
                    continue
                self.tasks_done.task_done()
        print('[OUTPUT] Terminating')
