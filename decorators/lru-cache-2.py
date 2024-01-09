# Rekurzivní výpočet Fibonacciho posloupnosti:
# - verze s LRU cache

from time import perf_counter
from functools import lru_cache


@lru_cache
def fib(n):
    """Rekurzivní výpočet Fibonacciho posloupnosti."""
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


max_n = 40

# opakovaný výpočet
for _ in range(10):
    start = perf_counter()
    result = fib(max_n)
    end = perf_counter()

    # tisk vypočteného výsledku i doby výpočtu
    print(result, end - start)
