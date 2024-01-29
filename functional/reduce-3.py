# Základy funkcionálního programování v Pythonu:
# - využití standardní funkce vyššího řádu "reduce"


# funkci reduce musíme explicitně naimportovat
from functools import reduce


def factorial(n):
    """Výpočet faktoriálu, interně založený na funkci reduce."""
    return reduce(lambda a, b: a * b, range(1, n + 1), 1)


# výpočet a zobrazení tabulky faktoriálů
for n in range(0, 11):
    print(n, factorial(n))
