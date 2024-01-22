# Synchronní běh:
# - vytvoření dvou ynchronních úloh
# - spuštění dvou úloh (jedna po druhé)
# - čekání na dokončení obou úloh
# - doba měření doby trvání běhu obou úloh

from time import perf_counter, sleep


# běžná synchronní funkce
def task(name):
    print(f"{name} task started")
    # ynchronní volání
    sleep(5)
    print(f"{name} task finished")


# běžná synchronní funkce
def main():
    # spuštění první úlohy
    task("first")

    # spuštění druhé úlohy
    task("second")

    print("done")


# měření času
start = perf_counter()

# přímé spuštění synchronní funkce
main()

# měření času
finish = perf_counter()

# výpis dosaženého času
print(f"Time elapsed: {finish-start : 5.1f}")
