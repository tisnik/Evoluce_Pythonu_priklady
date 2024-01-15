# Multiprocesing a multithreading v Pythonu:
# - vytvoření většího množství souběžných vláken
# - implicitní čekání na dokončení vláken
# - zjištění, ve kterém okamžiku se ukončí hlavní vlákno
# - zjištění, ve kterém okamžiku se zavolá destruktor objektu

import threading
import time


class X:
    def __init__(self):
        print("X constructed")

    def __del__(self):
        print("X destructed")


def worker():
    print("thread started")
    time.sleep(10)
    print("thread finished")


print("main started")

x = X()

# vytvoření a spuštění trojice vláken
threading.Thread(target=worker).start()
threading.Thread(target=worker).start()
threading.Thread(target=worker).start()

print("main finished")
