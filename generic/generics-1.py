# Generické datové typy v Pythonu:
# - definice funkce se dvěma parametry stejného typu
# - návratovou hodnotou je dvojice prvků stejného typu

from typing import Tuple, TypeVar

T = TypeVar('T')


def pair(first: T, second: T) -> Tuple[T, T]:
    x = (first, second)
    return x


print(pair("A", "B"))
