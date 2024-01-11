# Ukázka curryfikace (curryingu) funkce:
# - založeno na knihovně funcy
# - používá se "dopředná" curryfikace

from funcy import curry


def div(x, y):
    """Jednoduchá funkce se dvěma parametry."""
    return x / y


# curryfikace funkce div s využitím funkce curry
curried = curry(div)

# tisk informací o vrácené funkci
print("curried:", curried)

# zavolání vrácené funkce
print("curried(1):", curried(1))

# zavoláním se nám vrátí funkce, kterou opět
# můžeme zavolat
# (pozor na umístění závorek!)
print("curried(1)(2):", curried(1)(2))  # pozor na umístění závorek!
