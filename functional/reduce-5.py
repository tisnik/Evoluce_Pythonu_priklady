# Základy funkcionálního programování v Pythonu:
# - využití standardní funkce vyššího řádu "reduce"


# funkci reduce musíme explicitně naimportovat
from functools import reduce

# sekvence vstupních hodnot
n = range(0, 11)

# vypočítat hodnoty faktoriálů
factorials = map(lambda n: reduce(lambda a, b: a*b, range(1, n+1), 1), n)

# převod na seznam, který lze snadno vytisknout
print(list(factorials))
