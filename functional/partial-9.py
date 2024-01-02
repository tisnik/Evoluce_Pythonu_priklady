# Tisk atributů hodnoty, která je výsledkem transformace nějaké:
# - funkce s využitím funkce vyššího řádu `partial`.
# - varianta pro funkci s pojmenovanými argumenty

from functools import partial


def mul(x=1, y=1, z=1, w=1):
    """Funkce akceptující čtyři pojmenované parametry."""
    return x * y * z * w


def displayInfo(name, obj):
    """Tisk základních informací o předané hodnotě."""
    print("name:      ", name)
    print("function:  ", obj.func)
    print("arguments: ", obj.args)
    print("keywords:  ", obj.keywords)
    print()


# toto nelze pro běžnou funkci provést!
# f1 = mul
# displayInfo(f1())

# částečná aplikace - výsledkem bude funkce,
# do níž již byl dosazen první parametr.
f2 = partial(mul, x=2)

# tisk informace o vzniklém objektu
displayInfo("f2", f2)

# částečná aplikace - výsledkem bude nová funkce,
# do níž již byly dosazen druhý parametr.
f3 = partial(mul, y=2)

# tisk informace o vzniklém objektu
displayInfo("f3", f3)

# částečná aplikace - výsledkem bude nová funkce,
# do níž již byly dosazeny dva parametry.
f4 = partial(mul, y=2, z=2)

# tisk informace o vzniklém objektu
displayInfo("f4", f4)

# částečná aplikace - výsledkem bude nová funkce,
# do níž již byly dosazeny tři parametry.
f5 = partial(mul, x=2, y=2, z=2)

# tisk informace o vzniklém objektu
displayInfo("f5", f5)

# částečná aplikace - výsledkem bude nová funkce,
# do níž již byly dosazeny všechny čtyři parametry.
f6 = partial(mul, x=2, y=2, z=2, w=2)

# tisk informace o vzniklém objektu
displayInfo("f6", f6)
