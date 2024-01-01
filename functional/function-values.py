# Globální a lokální funkce


# globální funkce
def x():
    return


# funkce akceptující jiné funkce jako parametry
def add(x, y):
    return x() + y()


# funkce obsahující lokální funkci a vracející funkci
def local_values(foo):
    # lokální funkce
    def z():
        print("funkce z")

    if foo:
        # lokální funkce
        def w():
            print("funkce w")
        # vracíme lokální proměnnou - funkci
        return w

    # vracíme lokální proměnnou - funkci
    return z



funkce = local_values(False)
funkce()

funkce = local_values(True)
funkce()
