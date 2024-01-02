# Základní způsob použití funkce `partial` pro transformaci:
# - funkce se dvěma parametry na funkci s parametrem jediným.


from functools import partial


def mul(x, y):
    """Triviální funkce se dvěma parametry."""
    return x * y


# ukázka chování původní funkce
print(mul(6, 7))

print()

# částečná aplikace - výsledkem bude funkce
# akceptující jediný parametr y (x již bude rovno 2)
doubler = partial(mul, 2)


# ukázka použití nové funkce získané transformací
for i in range(11):
    print(i, doubler(i))
