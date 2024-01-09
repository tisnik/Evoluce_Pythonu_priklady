# Poziční a čistě poziční parametry funkcí:
# - pokus o zápis funkce bez čistě pozičních parametrů
# - tato chyba je zachycena interpretrem Pythonu


# chybná definice funkce bez čistě pozičních parametrů
def foo(/, x, y, z):
    return x+y-z


print(foo(1, 2, 10))
print(foo(z=1, y=2, x=10))
