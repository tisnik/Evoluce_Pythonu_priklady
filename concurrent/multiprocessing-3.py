# Multiprocesing a multithreading v Pythonu:
# - spuštění více úloh v nových procesech
# - komunikace mezi procesy s využitím fronty


from multiprocessing import Process, Queue
import time


def worker(name, q):
    while True:
        # čtení příkazů z fronty
        cmd = q.get()
        print(name, cmd)
        if cmd == "quit":
            print("Quitting")
            return
        time.sleep(1)


# vytvoření fronty pro komunikaci
q = Queue()

# vytvoření tří procesů
ps = [Process(target=worker, args=(name, q)) for name in ("foo", "bar", "baz")]

# spuštění tří procesů
for p in ps:
    p.start()

# komunikace přes frontu
for i in range(10):
    q.put("command {}".format(i))

# příkaz pro ukončení procesů
for i in range(3):
    q.put("quit")

# čekání na ukončení procesů
for p in ps:
    p.join()
