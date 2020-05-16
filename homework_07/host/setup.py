from host import MasterWorker
import signal


HOST = ('', 7777)
N_WORKERS = 4
BUFFER_SIZE = 64


if __name__ == '__main__':
    master = MasterWorker(N_WORKERS, BUFFER_SIZE)
    signal.signal(signal.SIGUSR1, master.terminate)
    master.engage(HOST)
