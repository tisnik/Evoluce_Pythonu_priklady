# Tisk atributů hodnoty, která je výsledkem transformace nějaké:
# - funkce s využitím funkce vyššího řádu `partial`.
# - varianta pro funkci s pozičními argumenty

from functools import partial


def mul(x, y, z, w):
    """Funkce akceptující čtyři poziční parametry."""
    return x * y * z * w


def display_info(name, obj):
    """Tisk základních informací o předané hodnotě."""
    print("name:      ", name)
    print("function:  ", obj.func)
    print("arguments: ", obj.args)
    print("keywords:  ", obj.keywords)
    print()


# toto nelze pro běžnou funkci provést!
# f1 = mul
# display_info(f1)

# částečná aplikace - výsledkem bude funkce,
# do níž již byl dosazen první parametr.
f2 = partial(mul, 2)

# tisk informace o vzniklém objektu
display_info("f2", f2)

# částečná aplikace - výsledkem bude funkce,
# do níž již byly dosazeny první dva parametry.
f3 = partial(mul, 2, 3)

# tisk informace o vzniklém objektu
display_info("f3", f3)

# částečná aplikace - výsledkem bude funkce,
# do níž již byly dosazeny první tři parametry.
f4 = partial(mul, 2, 3, 4)

# tisk informace o vzniklém objektu
display_info("f4", f4)

# částečná aplikace - výsledkem bude funkce,
# do níž již byly dosazeny všechny parametry.
f5 = partial(mul, 2, 3, 4, 5)

# tisk informace o vzniklém objektu
display_info("f5", f5)

# nekorektní transformace: tolik parametrů
# původní funkce neakceptuje!
f6 = partial(mul, 2, 3, 4, 5, 6)

# tisk informace o vzniklém objektu
display_info("f6", f6)
