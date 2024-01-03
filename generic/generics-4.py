# Generické datové typy v Pythonu:
# - nový způsob zápisu typových parametrů funkcí

from typing import Tuple


def pair[T, U](first: T, second: U) -> Tuple[T, U]:
    x = (first, second)
    return x


print(pair("A", "B"))
