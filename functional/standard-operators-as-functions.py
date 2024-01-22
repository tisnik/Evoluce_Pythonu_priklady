# Základy funkcionálního programování v Pythonu:
# - použití funkcí vyššího řádu
# - funkce vracející jinou funkci z balíčku operator


from operator import add, gt, lt, mul, pow


def get_operator(symbol):
    """Na základě předaného symbolu nalezne a vrátí příslušnou funkci."""
    operators = {
            "+": add,
            "*": mul,
            "^": pow,
            "<": lt,
            ">": gt,
    }
    return operators[symbol]


def calc(operator, x, y):
    """Aplikace předané funkce na parametry x a y."""
    return operator(x, y)


# získat funkci provádějící operaci "+" a následně tuto funkci zavolat
z = calc(get_operator("+"), 10, 20)
print(z)

# získat funkci provádějící operaci "*" a následně tuto funkci zavolat
z = calc(get_operator("*"), 10, 20)
print(z)

# získat funkci provádějící operaci "^" a následně tuto funkci zavolat
z = calc(get_operator("^"), 10, 20)
print(z)

# získat funkci provádějící operaci "<" a následně tuto funkci zavolat
z = calc(get_operator("<"), 10, 20)
print(z)

# získat funkci provádějící operaci ">" a následně tuto funkci zavolat
z = calc(get_operator(">"), 10, 20)
print(z)
