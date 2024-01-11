# Ukázka curryfikace (curryingu) funkce:
# - založeno na knihovně funcy
# - používá se "zpětná" curryfikace

from funcy import rcurry


def div(x, y):
    """Jednoduchá funkce se dvěma parametry."""
    return x / y


# curryfikace funkce div s využitím funkce rcurry
curried = rcurry(div)

# tisk informací o vrácené funkci
print(curried)

# zavolání vrácené funkce
print(curried(1))

# zavoláním se nám vrátí funkce, kterou opět
# můžeme zavolat
# (pozor na umístění závorek!)
print(curried(1)(2))  # pozor na umístění závorek!
