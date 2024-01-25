# Základní způsob použití funkce `partial` pro transformaci:
# - funkce akceptující libovolný počet parametrů.


import operator
from functools import partial, reduce


def mul(*args):
    """Funkce akceptující libovolný počet parametrů."""
    return reduce(operator.mul, args, 1)


# ukázka chování původní funkce
print(mul(2, 3, 7))

print()

# částečná aplikace - výsledkem bude funkce,
# do níž již byl dosazen první parametr.
doubler = partial(mul, 2)


# korektní způsob volání nové funkce získané transformací
# - předáváme jí jeden parametr
for i in range(11):
    print(i, doubler(i, 10))


print()


# částečná aplikace - výsledkem bude funkce,
# do níž již byly dosazeny dva parametry.
double_doubler = partial(mul, 2, 2)


# korektní způsob volání nové funkce získané transformací
# - předáváme jí jeden parametr
for i in range(11):
    print(i, double_doubler(i, 10))
