# Třída, jejíž instance mají atribut _enabled:
# - metoda set_enabled pro nastavení hodnoty tohoto atributu
# - speciální metoda __str__ pro získání textové reprezentace


class Foo:
    """Třída, jejíž instance mají atribut _enabled."""

    def __init__(self):
        self._enabled = False

    def set_enabled(self, state):
        """Nastavení hodnoty atributu _enabled."""
        self._enabled = state

    def __str__(self):
        """Získání textové reprezentace objektu."""
        return "Foo that is " + ("enabled" if self._enabled else "disabled")


# vytvoření instance
foo = Foo()
print(foo)
