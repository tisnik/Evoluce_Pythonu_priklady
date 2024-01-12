# Standardní operátor @property:
# - volání metod nepřímo - přes přístup k vlastnosti objektu

class Point:
    """Třída reprezentující bod v ploše."""

    def __init__(self, x, y):
        """Konstruktor s inicializací souřadnic bodu."""
        self._x = x
        self._y = y

    @property
    def x(self):
        """Vrácení x-ové souřadnice bodu."""
        return self._x

    @property
    def y(self):
        """Vrácení y-ové souřadnice bodu."""
        return self._y


# zkonstruovat bod
point = Point(2, 3)

# přečíst jeho souřadnice jakoby se jednalo o atributy
print(point.x, point.y)
