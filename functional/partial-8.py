# Základní způsob použití funkce `partial` pro transformaci:
# - funkce akceptující pojmenované parametry. Několika postupnými
#   transformacemi vzniknou funkce akceptující různý počet parametrů.

from functools import partial


def mul(x=1, y=1, z=1, w=1):
    """Funkce akceptující čtyři pojmenované parametry."""
    return x * y * z * w


# původní funkce
f1 = mul
print("f1:", f1())

# částečná aplikace - výsledkem bude funkce,
# do níž již byl dosazen první parametr.
f2 = partial(mul, x=2)
print("f2:", f2())

# částečná aplikace - výsledkem bude nová funkce,
# do níž již byly dosazen druhý parametr.
f3 = partial(mul, y=2)
print("f3:", f3())

# částečná aplikace - výsledkem bude nová funkce,
# do níž již byly dosazeny dva parametry.
f4 = partial(mul, y=2, z=2)
print("f4:", f4())

# částečná aplikace - výsledkem bude nová funkce,
# do níž již byly dosazeny tři parametry.
f5 = partial(mul, x=2, y=2, z=2)
print("f5:", f5())

# částečná aplikace - výsledkem bude nová funkce,
# do níž již byly dosazeny všechny čtyři parametry.
f6 = partial(mul, x=2, y=2, z=2, w=2)
print("f6:", f6())
