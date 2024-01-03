# Generické datové typy v Pythonu:
# - nový způsob zápisu typových parametrů funkcí
# - úprava pro novější verze Pythonu


def pair[T](first: T, second: T) -> tuple[T, T]:
    x = (first, second)
    return x


print(pair("A", "B"))
