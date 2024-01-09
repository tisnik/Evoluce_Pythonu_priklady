# Poziční a čistě poziční parametry funkcí:
# - definice a volání funkce s pozičními parametry
# - explicitní pojmenování parametrů při volání funkce


# funkce s pozičními parametry
def foo(x, y, z):
    return x+y-z


# explicitní specifikace parametrů jménem
# bez zachování jejich pořadí
print(foo(z=1, y=2, x=10))
