import socket
import time
from itertools import cycle


class RequestPuller:
    def __init__(self, urls):
        self.tasks = cycle(urls)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def engage(self, host, BUFFER_SIZE, working_status, timeout=None, connection_timeout=5, receive_timeout=10, FORMAT='utf-8'):
        self.working_status = True
        self.sock.connect(host)
        self.sock.settimeout(receive_timeout)
        while working_status.value:
            url = next(self.tasks)
            try:
                self.sock.send(url.encode(FORMAT))
                data = self.sock.recv(BUFFER_SIZE)
                if data:
                    data = data.decode(FORMAT)
                    true_length = BUFFER_SIZE - 33
                    real_length = len(data)
                    if real_length > true_length:
                        data = data[:real_length - true_length - 2]
                    if real_length < true_length:
                        data = data[:true_length - real_length - 2]
                    while data[-1] == 'X':
                        data = data[:-1]
                    size = int(data)
                    response = self.sock.recv(size).decode(FORMAT)
                else:
                    break
                with open('responses.txt', 'a') as file:
                    file.write(response + '\n' + '-' * 200 + '\n')
                if not timeout is None:
                    time.sleep(timeout)
            except (ConnectionRefusedError, ConnectionResetError):
                print('Host is offline, terminating')
            except socket.timeout:
                time.sleep(5)
                continue
        self.sock.close()
