# Třída, jejíž instance mají atribut _enabled:
# - metoda set_enabled pro nastavení hodnoty tohoto atributu
# - speciální metoda __str__ pro získání textové reprezentace
# - částečně aplikovaná metoda set_enabled
# - ukázka modifikace atributu přes tuto částečně aplikovanou metodu

from functools import partialmethod


class Foo:
    """Třída, jejíž instance mají atribut _enabled."""

    def __init__(self):
        """Konstruktor."""
        self._enabled = False

    def set_enabled(self, state):
        """Nastavení hodnoty atributu _enabled."""
        self._enabled = state

    # metody získané dosazením _druhého_ parametru
    enable = partialmethod(set_enabled, True)
    disable = partialmethod(set_enabled, False)

    def __str__(self):
        """Získání textové reprezentace objektu."""
        return "Foo that is " + ("enabled" if self._enabled else "disabled")


# vytvoření instance
foo = Foo()
print(foo)

# modifikace atributu přes částečně aplikovanou metodu
foo.enable()
print(foo)

# modifikace atributu přes částečně aplikovanou metodu
foo.disable()
print(foo)
