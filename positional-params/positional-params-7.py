# Poziční a čistě poziční parametry funkcí:
# - definice a volání funkce s jedním čistě pozičním parametrem


# funkce s jedním čistě pozičním parametrem
def foo(x, /, y, z):
    return x+y-z


# volání funkce s předáním argumentů
print(foo(1, 2, 10))

# argument pro parametr x se musí zadat pozičně
# ostatní argumenty již lze specifikovat se jménem
# parametru
print(foo(1, z=1, y=2))
