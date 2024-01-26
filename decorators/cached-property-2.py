# Výpočet n-tého prvku Fibonnaciho posloupnosti:
# - realizace formou třídy
# - výpočet se spustí přístupem k vlastnosti "value"
# - pokud se nečte tato vlastnost, výpočet vůbec neproběhne
# - opakované čtení vlastnosti již vrátí výsledek z vyrovnávací paměti

from functools import cached_property
from time import perf_counter


class FibonacciNumber:
    "Výpočet n-tého prvku Fibonnaciho posloupnosti." ""

    def __init__(self, n):
        """V konstruktoru si pouze zapamatujeme index prvku."""
        self._n = n

    @cached_property
    def value(self):
        """Metoda volaná jen jedenkrát."""
        return FibonacciNumber.compute(self._n)

    @staticmethod
    def compute(n):
        """Vlastní výpočet n-tého prvku posloupnosti."""
        if n < 2:
            return n
        return FibonacciNumber.compute(n - 1) + FibonacciNumber.compute(n - 2)


f = FibonacciNumber(40)

# opakované čtení vlastnosti "value"
for _ in range(10):
    start = perf_counter()
    result = f.value
    end = perf_counter()
    print(result, end - start)
