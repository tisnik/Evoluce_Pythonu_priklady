# Využití operace "unpack" při volání funkce s pěti argumenty


def add5(a, b, c, d, e):
    """Funkce akceptující pět parametrů."""
    print(f"Adding {a} + {b} + {c} + {d} + {e}")
    return a+b+c+d+e


l1 = [1, 2]
l2 = [4, 5]

# různé varianty rozbalení obsahu seznamů
x = add5(*l1, 3, *l2)
y = add5(*l1, *l2, 10)
z = add5(100, *l1, *l2)

print("x:", x)
print("y:", y)
print("z:", z)
