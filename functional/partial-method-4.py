# Třída, jejíž instance mají atributy _x a _y:
# - metoda move_to pro nastavení hodnot těchto atributů
# - speciální metoda __str__ pro získání textové reprezentace
# - částečně aplikovaná metoda move_to
# - ukázka modifikace atributů přes tuto částečně aplikovanou metodu

from functools import partialmethod


class Point:
    """Třída, jejíž instance mají atributy _x a _y."""

    def __init__(self):
        self._x = 0
        self._y = 0

    def move_to(self, x, y):
        """Nastavení hodnoty atributů _x a _y."""
        self._x = x
        self._y = y

    # metoda získaná dosazením druhého a třetího parametru
    to_origin = partialmethod(move_to, 0, 0)

    def __str__(self):
        """Získání textové reprezentace objektu."""
        return f"Point[{self._x}, {self._y}]"


# vytvoření instance bodu
point = Point()
print(point)

# přímé volání metody move_to
point.move_to(1, 2)
print(point)

# volání částečně aplikované metody move_to
point.to_origin()
print(point)
