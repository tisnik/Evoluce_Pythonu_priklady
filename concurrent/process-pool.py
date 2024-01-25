# Multiprocesing a multithreading v Pythonu:
# - spouštění úloh v procesech s využitím třídy ProcessPoolExecutor

import time
from concurrent.futures import ProcessPoolExecutor


def worker(process_name, delay, n):
    for counter in range(1, n + 1):
        time.sleep(delay)
        print("{}: {}/{} - {}".format(process_name, counter, n, time.ctime(time.time())))


# spuštění tří úloh, každé v samostatném procesu
with ProcessPoolExecutor(max_workers=3) as executor:
    executor.submit(worker, "Process-1", 0.5, 10)
    executor.submit(worker, "Process-2", 1.0, 10)
    executor.submit(worker, "Process-3", 1.5, 10)


print("Done!")
