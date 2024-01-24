# Multiprocesing a multithreading v Pythonu:
# - spuštění více úloh v nových procesech
# - čekání na dokončení procesů

import time
from multiprocessing import Process


def worker(name):
    print("hello", name)
    time.sleep(5)
    print("done", name)


ps = []

for name in ("foo", "bar", "baz", "other"):
    p = Process(target=worker, args=(name,))
    p.start()
    ps.append(p)

for p in ps:
    p.join()
