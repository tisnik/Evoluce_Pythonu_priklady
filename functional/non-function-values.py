# Globální a lokální proměnné


# globální proměnná
x = 10


# funkce akceptující parametry
def add(x, y):
    return x + y


# funkce obsahující lokální proměnné a vracející jejich obsah
def local_values(foo):
    # lokální proměnná
    z = 10
    print(z)

    if foo:
        # lokální proměnná
        w = 20
        print(w)
        # vracíme lokální proměnnou
        return w

    # vracíme lokální proměnnou
    return z
