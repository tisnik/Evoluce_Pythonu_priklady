# Rekurzivní výpočet Fibonacciho posloupnosti:
# - verze s cache

from functools import cache
from time import perf_counter


@cache
def fib(n):
    """Rekurzivní výpočet Fibonacciho posloupnosti."""
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


max_n = 300

# opakovaný výpočet
for i in range(20):
    # vymazání cache
    if i % 5 == 0:
        fib.cache_clear()

    print(fib.cache_info())
    start = perf_counter()
    result = fib(max_n)
    end = perf_counter()

    # tisk vypočteného výsledku i doby výpočtu
    print(result, end - start)

# vymazání cache
fib.cache_clear()
