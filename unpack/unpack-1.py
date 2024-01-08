# Operátor "unpack" v Pythonu:
# - explicitní předání dvou parametrů do funkce add
# - (unpack se zde prozatím nepoužívá)


def add(x, y):
    """Funkce akceptující dva parametry."""
    print(f"Adding {x} + {y}")
    return x+y


lst = [1, 2]

x = add(lst[0], lst[1])
print(x)
