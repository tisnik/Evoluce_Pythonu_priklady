# Multiprocesing a multithreading v Pythonu:
# - spuštění úlohy v novém procesu
# - čekání na dokončení procesů

from multiprocessing import Process


def worker(name):
    print("hello", name)


# vytvoření úlohy s předáním parametrů
p = Process(target=worker, args=("foo",))

# spuštění úlohy
p.start()

# čekání na dokončení úlohy
p.join()
