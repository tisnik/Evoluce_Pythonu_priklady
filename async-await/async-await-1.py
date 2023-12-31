# Využití standardní knihovny asyncio:
# - vytvoření asynchronní úlohy
# - spuštění této úlohy
# - čekání na dokončení této úlohy
# - prozatím nefunkční řešení kvůli způsobu volání main!

import asyncio


# funkce, která dokáže dočasně předat řízení přes await
async def task():
    print("task started")
    # asynchronní volání - interpret může vykonávat jinou činnost
    await asyncio.sleep(5)
    print("task finished")


# běžná funkce
def main():
    # jedna z možnosti spuštění úlohy
    task1 = asyncio.create_task(task())
    print("task created")

    # (problém) - čekání na dokončení úlohy
    await task1

    print("done")


main()
