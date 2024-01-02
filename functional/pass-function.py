# Základní použití funkcí vyššího řádu:
# - předání funkce do jiné funkce


def calc(operator, x, y):
    """Aplikace předané funkce na parametry x a y."""
    return operator(x, y)


def add(x, y):
    """Funkce pro součet dvou hodnot."""
    return x + y


def mul(x, y):
    """Funkce pro součin dvou hodnot."""
    return x * y


def less_than(x, y):
    """Funkce pro porovnání dvou hodnot na relaci "menší než"."""
    return x < y


def greater_than(x, y):
    """Funkce pro porovnání dvou hodnot na relaci "větší než"."""
    return x > y


# předání funkce add
z = calc(add, 10, 20)
print(z)

# předání funkce mull
z = calc(mul, 10, 20)
print(z)

# předání funkce less_than
z = calc(less_than, 10, 20)
print(z)

# předání funkce greater_than
z = calc(greater_than, 10, 20)
print(z)
