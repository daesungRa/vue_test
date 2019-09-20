
import threading
import time
from random import *


def sample_thread(sec):
    print(f'Start {threading.currentThread().getName()} in {sec} second(s).')
    time.sleep(sec)
    print(f'End {threading.currentThread().getName()}.')


if __name__ == '__main__':
    print('=== Start Process!! ===')
    start_time = time.perf_counter()

    thread_list = []
    secs = [randint(1, 10) for _ in range(5)]
    for s in secs:
        thread_list.append(threading.Thread(target=sample_thread, args=(s,)))
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()

    end_time = time.perf_counter()
    print(f'=== End Process. It takes {round(end_time - start_time, 2)} second(s) ===')
