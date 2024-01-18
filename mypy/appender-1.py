# Typové anotace a nástroj Mypy:
# - funkce append bez typových anotací
# - volání funkce s argumenty nesprávných typů
#   (hodnoty 1 a 2 nemají metodu strip)


def append(a, b):
    return a.strip()+b.strip()


print(append(1, 2))
