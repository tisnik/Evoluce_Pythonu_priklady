# Zavolání funkce s rozbalením slovníku operací unpack


def add3(x, y, z):
    """Funkce akceptující tři parametry."""
    print(f"Adding {x} + {y} + {z}")
    return x+y+z


d = {"x": 1,
     "y": 2,
     "z": 3}

# rozhalení slovníku
print(add3(**d))
