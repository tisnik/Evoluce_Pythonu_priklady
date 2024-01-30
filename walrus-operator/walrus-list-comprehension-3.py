# Mroží operátor v Pythonu:
# - dvojí volání Ackermannovy funkce pro
#   každou dvojici parametrů

from time import perf_counter


def A(m, n):
    """Ackermannova funkce."""
    if m == 0:
        return n + 1
    if n == 0:
        return A(m - 1, 1)
    return A(m - 1, A(m, n - 1))


start = perf_counter()

results = [A(m, n) for m in range(0, 4) for n in range(0, 7) if A(m, n) % 2 != 0]

print(results)

finish = perf_counter()

print(f"Duration: {finish-start} seconds")
