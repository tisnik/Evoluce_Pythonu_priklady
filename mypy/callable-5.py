# Typové anotace a nástroj Mypy:
# - funkci printIsPositive lze předat jinou funkci
# - parametr "condition" má zapsán datový typ
# - testování typu variance

from typing import Callable


def printIsPositive(condition:Callable[[float], bool]) -> None:
    if condition(5):
        print("Positive")
    else:
        print("Negative")


def positiveFloat(x:float) -> bool:
    return x > 0.0


def positiveInt(x:int) -> bool:
    return x > 0


# do funkce printIsPositive můžeme předat jen funkci
# s argumentem typu float
printIsPositive(positiveFloat)
printIsPositive(positiveInt)
