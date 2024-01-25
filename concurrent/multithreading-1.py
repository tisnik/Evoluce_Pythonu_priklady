# Multiprocesing a multithreading v Pythonu:
# - vytvoření většího množství vláken
# - implicitní čekání na dokončení vláken

import threading
import time


def worker():
    thread_name = threading.current_thread().name
    delay = 1
    n = 10
    for counter in range(1, n + 1):
        time.sleep(delay)
        print("{}: {}/{} - {}".format(thread_name, counter, n, time.ctime(time.time())))


# vytvoření a spuštění trojice vláken
threading.Thread(target=worker).start()
threading.Thread(target=worker).start()
threading.Thread(target=worker).start()
