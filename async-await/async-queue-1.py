# Využití standardní knihovny asyncio:
# - příprava dat pro úlohy
# - komunikace mezi úlohami přes frontu
# - spuštění asynchronních úloh
# - bez čekání na dokončení (zpětné přečtení výsledků)

import asyncio


# vykonání úloh, jejichž parametry jsou přečteny z fronty
async def task(name, queue):
    print(f"\tCoroutine #{name} started")
    while not queue.empty():
        param = await queue.get()
        print(f"\t\tTask with parameter {param : 5.2f} started")
        await asyncio.sleep(5)
        print(f"\t\tTask with parameter {param : 5.2f} finished")
    print(f"\tCoroutine #{name} finished")


# funkce, která dokáže dočasně předat řízení přes await
async def main():
    print("Main started")
    queue = asyncio.Queue()

    for i in range(10):
        await queue.put(1/(i+1))

    for n in range(1, 11):
        asyncio.create_task(task(f"{n}", queue))

    print("Main finished")


# spuštění funkce, jenž je definována s async
asyncio.run(main())
