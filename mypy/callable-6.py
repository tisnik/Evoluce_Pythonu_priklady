# Typové anotace a nástroj Mypy:
# - funkci printIsPositive lze předat jinou funkci
# - parametr "condition" má zapsán datový typ
# - testování typu variance
# - oprava příkladu s využitím kovariance

from typing import Callable


def printIsPositive(condition:Callable[[int], bool]) -> None:
    if condition(5):
        print("Positive")
    else:
        print("Negative")


def positiveFloat(x:float) -> bool:
    return x > 0.0


def positiveInt(x:int) -> bool:
    return x > 0


# do funkce printIsPositive můžeme předat jak funkci
# s argumentem typu float, tak i funkci s argumentem
# typu int
printIsPositive(positiveFloat)
printIsPositive(positiveInt)
