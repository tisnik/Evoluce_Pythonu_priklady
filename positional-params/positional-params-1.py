# Poziční a čistě poziční parametry funkcí:
# - definice a volání funkce s pozičními parametry


# funkce s pozičními parametry
def foo(x, y, z):
    return x + y - z


# volání funkce s předáním argumentů
print(foo(1, 2, 10))

# explicitní specifikace parametrů jménem
# se zachováním jejich pořadí
print(foo(x=1, y=2, z=10))
