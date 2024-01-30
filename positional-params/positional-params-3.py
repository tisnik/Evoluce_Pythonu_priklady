# Poziční a čistě poziční parametry funkcí:
# - definice a volání funkce s čistě pozičními parametry
# - pokus o zavolání funkce s pojmenováním parametrů


# funkce s čistě pozičními parametry
def foo(x, y, z, /):
    return x + y - z


# volání funkce s předáním argumentů
print(foo(1, 2, 10))

# explicitní specifikace parametrů jménem
# není povolena (nezávisle na pořadí)
print(foo(x=1, y=2, z=10))
print(foo(z=1, y=2, x=10))
