# Kompozice funkcí:
# - založeno na knihovně funcy
# - používá se funkce compose

from funcy import compose


def add(x, y):
    """Běžná funkce se dvěma argumenty."""
    return x + y


def double(x):
    """Běžná funkce s jediným argumentem."""
    return 2 * x


# kompozice dvou výše uvedených funkcí
composed = compose(double, add)

# součet následovaný zdvojnásobením hodnoty
print(composed(2, 3))
print(composed(-2, -3))
