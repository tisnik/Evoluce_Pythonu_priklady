# Generické datové typy v Pythonu:
# - definice funkce se dvěma parametry obecně odlišného typu
# - návratovou hodnotou je dvojice prvků odlišného typu

from typing import Tuple, TypeVar

T = TypeVar("T")
U = TypeVar("U")


def pair(first: T, second: U) -> Tuple[T, U]:
    x = (first, second)
    return x


reveal_type(pair(1, 2))
reveal_type(pair(0, "B"))
reveal_type(pair("A", 42))
reveal_type(pair("A", "B"))
