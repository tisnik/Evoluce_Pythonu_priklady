# Základy funkcionálního programování v Pythonu:
# - využití standardní funkce vyššího řádu "reduce"


# funkci reduce musíme explicitně naimportovat
from functools import reduce


# sekvence numerických hodnot
x = range(1, 11)
print(x)

# postupná "redukce" sekvence s akumulací mezivýsledků
y = reduce(lambda a, b: a*b, x)
print(y)
