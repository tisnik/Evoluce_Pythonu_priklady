# Využití standardní knihovny asyncio:
# - vytvoření tří asynchronních úloh
# - spuštění úloh
# - čekání na dokončení všech tří úloh
# - tisk výsledků získaných z úloh

import asyncio


# funkce, která dokáže dočasně předat řízení přes await
async def task(name):
    print(f"{name} task started")
    # asynchronní volání - interpret může vykonávat jinou činnost
    await asyncio.sleep(5)
    print(f"{name} task finished")

    # vrátíme hodnotu volající (čekající) funkci
    return name[::-1]


# funkce, která dokáže dočasně předat řízení přes await
async def main():
    # spuštění první úlohy
    task1 = asyncio.create_task(task("first"))
    print("first task created")

    # spuštění druhé úlohy
    task2 = asyncio.create_task(task("second"))
    print("second task created")

    # spuštění třetí úlohy
    task3 = asyncio.create_task(task("third"))
    print("third task created")

    # čekání na dokončení úloh s výpisem vypočtených výsledků
    print("result of task #1:", await task1)
    print("result of task #2:", await task2)
    print("result of task #3:", await task3)

    print("done")


# spuštění funkce, jenž je definována s async
asyncio.run(main())
