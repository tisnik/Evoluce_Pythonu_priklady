# Ukázka curryfikace (curryingu) funkce:
# - založeno na knihovně funcy

from funcy import curry


def add(x, y):
    """Jednoduchá funkce se dvěma parametry."""
    return x + y


# curryfikace funkce add
curried = curry(add)

# tisk informací o vrácené funkci
print("curried:", curried)

# zavolání vrácené funkce
print("curried(1):", curried(1))

# zavoláním se nám vrátí funkce, kterou opět
# můžeme zavolat
# (pozor na umístění závorek!)
print("curried(1)(2):", curried(1)(2))
