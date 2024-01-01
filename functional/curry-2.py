# Ukázka curryfikace (curryingu) funkce:
# - založeno na knihovně funcy

from funcy import curry


def add3(x, y, z):
    """Jednoduchá funkce se třemi parametry."""
    return x + y + z


# curryfikace funkce add3
curried = curry(add3)

# tisk informací o vrácené funkci
print("curried:", curried)

# zavolání vrácené funkce
print("curried(1):", curried(1))

# zavoláním se nám vrátí funkce, kterou opět
# můžeme zavolat
# (pozor na umístění závorek!)
print("curried(1)(2):", curried(1)(2))

# totéž lze provést ještě jednou
# (opět pozor na umístění závorek!)
print("curried(1)(2)(3):", curried(1)(2)(3))
