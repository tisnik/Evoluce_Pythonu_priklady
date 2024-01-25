# Ukázka autocurryfikace (curryingu) funkce:
# - založeno na knihovně funcy

from funcy import autocurry


def pow(x, y):
    """Jednoduchá funkce se dvěma parametry."""
    return x ** y


# autocurryfikace funkce pow
n_pow = autocurry(pow)

# různé způsoby využití objektu n_pow, který jsme získali

# de facto původní funkce (i když interně odlišná)
pow_x = n_pow()

# částečně aplikované funkce
pow2 = n_pow(2)
pow10 = n_pow(10)

# volání funkce s výsledkem 3^3
pow3to3 = n_pow(3, 3)

print("powX:", pow_x(3, 3))
print("pow2:", pow2(2))
print("pow10:", pow10(2))
print("pow3to3:", pow3to3)
