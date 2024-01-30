# Poziční a čistě poziční parametry funkcí:
# - definice a volání funkce s jedním čistě pozičním parametrem


# funkce s jedním čistě pozičním parametrem
def foo(x, /, y, z):
    return x + y - z


# volání funkce s předáním argumentů
print(foo(1, 2, 10))

# explicitní specifikace parametru y a z jménem
# je povolena
print(foo(1, 2, z=10))
print(foo(1, y=2, z=10))

# explicitní specifikace parametru x jménem
# není povolena (nezávisle na pořadí)
print(foo(x=1, y=2, z=10))
print(foo(z=1, y=2, x=10))
