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


def abs(x):
    """Běžná funkce s jediným argumentem."""
    if x < 0:
        return -x
    return x


# kompozice všech tří výše uvedených funkcí
composed = compose(abs, double, add)

# součet následovaný zdvojnásobením hodnoty
# jenž je následovaný výpočtem absolutní hodnoty
print(composed(2, 3))
print(composed(-2, -3))
