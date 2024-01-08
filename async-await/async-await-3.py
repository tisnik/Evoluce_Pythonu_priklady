# Využití standardní knihovny asyncio:
# - vytvoření dvou asynchronních úloh
# - spuštění obou těchto úloh
# - čekání na dokončení obou těchto úloh

import asyncio


# funkce, která dokáže dočasně předat řízení přes await
async def task(name):
    print(f"{name} task started")
    # asynchronní volání - interpret může vykonávat jinou činnost
    await asyncio.sleep(5)
    print(f"{name} task finished")


# funkce, která dokáže dočasně předat řízení přes await
async def main():
    # spuštění první úlohy
    task1 = asyncio.create_task(task("first"))
    print("first task created")

    # spuštění druhé úlohy
    task2 = asyncio.create_task(task("second"))
    print("second task created")

    # čekání na dokončení úloh
    await task1
    await task2

    print("done")


# spuštění funkce, jenž je definována s async
asyncio.run(main())
