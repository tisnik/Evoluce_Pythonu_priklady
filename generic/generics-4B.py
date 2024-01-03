# Generické datové typy v Pythonu:
# - nový způsob zápisu typových parametrů funkcí
# - úprava pro novější verze Pythonu


def pair[T, U](first: T, second: U) -> tuple[T, U]:
    x = (first, second)
    return x


print(pair("A", "B"))
