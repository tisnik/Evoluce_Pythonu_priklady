# Využití standardní knihovny asyncio:
# - vytvoření asynchronní úlohy
# - spuštění úlohy
# - čekání na dokončení úlohy
# - korektní volání funkce main

import asyncio


# funkce, která dokáže dočasně předat řízení přes await
async def task():
    print("task started")
    # asynchronní volání - interpret může vykonávat jinou činnost
    await asyncio.sleep(5)
    print("task finished")


# funkce, která dokáže dočasně předat řízení přes await
async def main():
    # jedna z možnosti spuštění úlohy
    task1 = asyncio.create_task(task())
    print("task created")

    # čekání na dokončení úlohy
    await task1

    print("done")


# spuštění funkce, jenž je definována s async
asyncio.run(main())
