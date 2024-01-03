# Generické datové typy v Pythonu:
# - definice funkce se dvěma parametry stejného typu
# - návratovou hodnotou je dvojice prvku stejného typu
# - úprava pro novější verze Pythonu

from typing import TypeVar

T = TypeVar('T')


def pair(first: T, second: T) -> tuple[T, T]:
    x = (first, second)
    return x


print(pair("A", "B"))
