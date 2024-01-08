# Operátor "unpack" v Pythonu:
# - zavolání funkce s rozbalením slovníku operací unpack


def add3(x, y, z):
    """Funkce akceptující tři parametry."""
    print(f"Adding {x} + {y} + {z}")
    return x+y+z


d = {"z": 3,
     "y": 2,
     "x": 1}

# rozhalení slovníku
print(add3(**d))
