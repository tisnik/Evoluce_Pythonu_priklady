# Explicitní předání dvou parametrů do funkce add


def add(x, y):
    """Funkce akceptující dva parametry."""
    print(f"Adding {x} + {y}")
    return x+y


lst = [1, 2]

x = add(lst[0], lst[1])
print(x)
