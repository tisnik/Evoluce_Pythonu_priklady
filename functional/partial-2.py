# Základní způsob použití funkce `partial` pro transformaci:
# - funkce se třemi parametry na funkci se dvěma parametry.


from functools import partial


def mul(x, y, z):
    """Triviální funkce se třemi parametry."""
    return x * y * z


# ukázka chování původní funkce
print(mul(2, 3, 7))

print()

# částečná aplikace - výsledkem bude funkce
# akceptující dva parametry (x je již rovno 2)
doubler = partial(mul, 2)


# nekorektní způsob volání nové funkce získané transformací
# - předáváme jí jediný parametr
for i in range(11):
    print(i, doubler(i))
