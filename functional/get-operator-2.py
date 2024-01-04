# Základní použití funkcí vyššího řádu:
# - funkce vracející jinou funkci


def get_operator(symbol):
    """Na základě předaného symbolu nalezne a vrátí příslušnou funkci."""
    operators = {
            "+": add,
            "*": mul,
            "<": less_than,
            ">": greater_than,
    }
    return operators[symbol]


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


# získat funkci provádějící operaci "+" a následně tuto funkci zavolat
z = calc(get_operator("+"), 10, 20)
print(z)

# získat funkci provádějící operaci "*" a následně tuto funkci zavolat
z = calc(get_operator("*"), 10, 20)
print(z)

# získat funkci provádějící operaci "<" a následně tuto funkci zavolat
z = calc(get_operator("<"), 10, 20)
print(z)

# získat funkci provádějící operaci ">" a následně tuto funkci zavolat
z = calc(get_operator(">"), 10, 20)
print(z)
