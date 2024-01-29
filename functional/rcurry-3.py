# Praktické použití curryfikace pro konstrukci
# funkcí pro výpočet n-té mocniny předaného základu

from funcy import rcurry


def pow(x, y):
    """Výpočet x^y."""
    return x**y


# "zpětná" curryfikace funkce pow s využitím funkce rcurry
n_pow = rcurry(pow)

# necháme si vytvořit funkci pro výpočet druhé mocniny
pow2 = n_pow(2)

# necháme si vytvořit funkci pro výpočet třetí mocniny
pow3 = n_pow(3)

# a taktéž si necháme vytvořit funkci pro výpočet desáté mocniny
pow10 = n_pow(10)

# otestování všech tří funkcí
print(" n   n^2   n^3         n^10")

for n in range(1, 11):
    print(f"{n:2}  {pow2(n):4}  {pow3(n):4}  {pow10(n):11}")
