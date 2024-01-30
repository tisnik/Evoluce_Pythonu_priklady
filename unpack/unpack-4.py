# Operátor "unpack" v Pythonu:
# - využití operace "unpack" při volání funkce s pěti argumenty


def add5(a, b, c, d, e):
    """Funkce akceptující pět parametrů."""
    print(f"Adding {a} + {b} + {c} + {d} + {e}")
    return a + b + c + d + e


# různé varianty rozbalení řady vytvářené generátorem
x = add5(*range(5))
y = add5(*range(4), 100)
z = add5(*range(3), *range(10, 12))

print("x:", x)
print("y:", y)
print("z:", z)
