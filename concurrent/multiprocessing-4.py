# Multiprocesing a multithreading v Pythonu:
# - spuštění více úloh v nových procesech
# - komunikace mezi procesy s obousměrné fronty


from multiprocessing import Process, Pipe
import time


def worker(name, conn):
    while True:
        # čtení příkazu z prvního procesu
        cmd = conn.recv()
        print("{} received {}".format(name, cmd))
        if cmd == "quit":
            return
        else:
            conn.send("{} accepted {}".format(name, cmd))
        time.sleep(1)


# vytvoření komunikační roury (má dva konce)
parent_conn, child_conn = Pipe()

# spuštění dalšího procesu
p = Process(target=worker, args=("Worker", child_conn))
p.start()

# komunikace s procesem
for i in range(10):
    parent_conn.send("command {}".format(i))
    print(parent_conn.recv())

# poslání příkazu pro ukončení druhého procesu
parent_conn.send("quit")

# čekání na dokončení druhého procesu
p.join()
