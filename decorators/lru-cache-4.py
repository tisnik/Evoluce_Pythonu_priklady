# Rekurzivní výpočet Fibonacciho posloupnosti:
# - verze s LRU cache
# - průběžné vymazání LRU cache

from functools import lru_cache
from time import perf_counter


@lru_cache
def fib(n):
    """Rekurzivní výpočet Fibonacciho posloupnosti."""
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


max_n = 40

# opakovaný výpočet
for i in range(15):
    # vymazání cache
    if i % 5 == 0:
        fib.cache_clear()
    print(fib.cache_info())
    start = perf_counter()
    result = fib(max_n)
    end = perf_counter()

    # tisk vypočteného výsledku i doby výpočtu
    print(result, end - start)

print(fib.cache_info())
