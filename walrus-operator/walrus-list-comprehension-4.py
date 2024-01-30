# Mroží operátor v Pythonu:
# - optimalizované volání Ackermannovy funkce
#   pro každou dvojici parametrů.

from time import perf_counter


def A(m, n):
    """Ackermannova funkce."""
    if m == 0:
        return n + 1
    if n == 0:
        return A(m - 1, 1)
    return A(m - 1, A(m, n - 1))


# zjistit čas před výpočtem
start = perf_counter()

results = [result for m in range(4) for n in range(7) if (result := A(m, n)) % 2 != 0]

print(results)

# zjistit čas po výpočtu
finish = perf_counter()

# zobrazení celkové doby výpočtu
print(f"Duration: {finish-start} seconds")
