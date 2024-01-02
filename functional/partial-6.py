# Základní způsob použití funkce `partial` pro transformaci:
# - funkce akceptující čtyři parametry. Několika postupnými transformacemi
#   vzniknou funkce akceptující různý počet parametrů.

from functools import partial


def mul(x, y, z, w):
    """Funkce akceptující čtyři parametry."""
    return x * y * z * w


# původní funkce
f1 = mul
print("f1:", f1)

# částečná aplikace - výsledkem bude funkce,
# do níž již byl dosazen první parametr.
f2 = partial(f1, 2)
print("f2:", f2)

# částečná aplikace na částečně aplikovanou funkci
# - výsledkem bude nová funkce,
#   do níž již byly dosazeny první dva parametry.
f3 = partial(f2, 3)
print("f3:", f3)

# částečná aplikace na částečně aplikovanou funkci
# - výsledkem bude nová funkce,
#   do níž již byly dosazeny první tři parametry.
f4 = partial(f3, 4)
print("f4:", f4)

# částečná aplikace na částečně aplikovanou funkci
# - výsledkem bude nová funkce,
#   do níž již byly dosazeny všechny čtyři parametry.
f5 = partial(f4, 5)
print("f5:", f5)

# částečná aplikace na částečně aplikovanou funkci
# - výsledkem bude nová funkce,
#   do níž již bylo dosazeny pět parametrů.
f6 = partial(f5, 6)
print("f6:", f6)

# nově vzniklé funkce se pokusíme zavolat
print("\ncalls:")

print("f1:", f1(2, 3, 4, 5))
print("f2:", f2(3, 4, 5))
print("f3:", f3(4, 5))
print("f4:", f4(5))
print("f5:", f5())
print("f6:", f6())
