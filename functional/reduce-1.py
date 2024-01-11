# Základy funkcionálního programování v Pythonu:
# - využití standardní funkce vyššího řádu "reduce"


# funkci reduce musíme explicitně naimportovat
from functools import reduce


def multiply(x, y):
    """Součin dvou hodnot předaných do funkce."""
    return x * y


# sekvence numerických hodnot
x = range(1, 11)
print(x)

# postupná "redukce" sekvence s akumulací mezivýsledků
y = reduce(multiply, x)
print(y)
