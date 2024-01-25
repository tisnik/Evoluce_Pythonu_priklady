# Multiprocesing a multithreading v Pythonu:
# - vytvoření většího množství souběžných vláken
# - implicitní čekání na dokončení vláken

import threading
import time


def worker(thread_name, delay, n):
    for counter in range(1, n + 1):
        time.sleep(delay)
        print("{}: {}/{} - {}".format(thread_name, counter, n, time.ctime(time.time())))


# vytvoření a spuštění trojice vláken
threading.Thread(target=worker, args=("Thread-1", 0.5, 10)).start()
threading.Thread(target=worker, args=("Thread-2", 1.0, 10)).start()
threading.Thread(target=worker, args=("Thread-3", 1.5, 10)).start()
