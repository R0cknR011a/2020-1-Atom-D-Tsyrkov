from puller import RequestPuller
from multiprocessing import Process, Value
from ctypes import c_bool
import signal
import os


URLS = ['http://python.org', 'http://docs.python.org', 'http://stackoverflow.com', 'http://geeksforgeeks.org', 'https://mail.ru']
HOST = ('localhost', 7777)
USERS = 10
BUFFER_SIZE = 64

processes = []
working_status = Value(c_bool, True)
for _ in range(USERS):
    puller = RequestPuller(URLS)
    p = Process(target=puller.engage, args=(HOST, BUFFER_SIZE, working_status))
    processes.append(p)

def terminate(signal_num, frame):
    working_status.value = False

if __name__ == '__main__':
    signal.signal(signal.SIGUSR1, terminate)
    for p in processes:
        p.start()
    print(f'STARTED WITH ID: {os.getpid()}')
    for p in processes:
        p.join()
