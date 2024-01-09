# Poziční a čistě poziční parametry funkcí:
# - definice a volání funkce se dvěma čistě pozičními parametry


# funkce se dvěma čistě pozičními parametry
def foo(x, y, /, z):
    return x+y-z


# volání funkce s předáním argumentů
print(foo(1, 2, 10))


# explicitní specifikace parametru z jménem
# je povolena
print(foo(1, 2, z=10))

# explicitní specifikace parametrů x a y jménem
# není povolena (nezávisle na pořadí)
print(foo(x=1, y=2, z=10))
print(foo(z=1, y=2, x=10))
