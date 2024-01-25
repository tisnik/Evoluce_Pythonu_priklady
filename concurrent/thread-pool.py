# Multiprocesing a multithreading v Pythonu:
# - spouštění úloh ve vláknech s využitím třídy ThreadPoolExecutor

import time
from concurrent.futures.thread import ThreadPoolExecutor


def worker(thread_name, delay, n):
    for counter in range(1, n + 1):
        time.sleep(delay)
        print("{}: {}/{} - {}".format(thread_name, counter, n, time.ctime(time.time())))


# spuštění tří úloh, každé v samostatném vlákně
with ThreadPoolExecutor(max_workers=3) as executor:
    executor.submit(worker, "Thread-1", 0.5, 10)
    executor.submit(worker, "Thread-2", 1.0, 10)
    executor.submit(worker, "Thread-3", 1.5, 10)


print("Done!")
