# Využití operace "unpack" při volání funkce se dvěma parametry


def add(x, y):
    """Funkce akceptující dva parametry."""
    print(f"Adding {x} + {y}")
    return x+y


lst = [1, 2]

x = add(*lst)
print(x)
