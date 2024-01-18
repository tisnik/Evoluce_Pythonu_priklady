# Typové anotace a nástroj Mypy:
# - funkce append s typovými anotacemi
# - buď je chyba v typových anotacích nebo ve volání metody strip


def append(a:int, b:int) -> int:
    return a.strip()+b.strip()
