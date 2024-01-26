# Použití standardního dekorátoru @total_ordering

from functools import total_ordering


@total_ordering
class Version:
    """Třída reprezentující verzi ve formě major.minor.patch."""

    def __init__(self, major, minor=0, patch=0):
        """Konstruktor s inicializací verze."""
        self._major = major
        self._minor = minor
        self._patch = patch

    def _is_valid_version(self, other):
        """Test, zda předaný objekt obsahuje zmíněné atributy."""
        return (
            hasattr(other, "_major")
            and hasattr(other, "_minor")
            and hasattr(other, "_patch")
        )

    def __eq__(self, other):
        """Metoda implementující operátor ==."""
        if not self._is_valid_version(other):
            return NotImplemented
        return (self._major, self._minor, self._patch) == (
            other._major,
            other._minor,
            other._patch,
        )

    def __lt__(self, other):
        """Metoda implementující operátor <."""
        if not self._is_valid_version(other):
            return NotImplemented
        return (self._major, self._minor, self._patch) < (
            other._major,
            other._minor,
            other._patch,
        )

    def __str__(self):
        """Textová reprezentace objektu."""
        return f"{self._major}.{self._minor}.{self._patch}"


# konstrukce několika instancí třídy Version
v1 = Version(1, 0, 0)
v2 = Version(1, 0, 1)
v3 = Version(1, 2, 0)
v4 = Version(2, 1, 0)

print("v1:", v1)
print("v2:", v2)
print("v3:", v3)
print("v4:", v4)
print()

print("v1 == v2:", v1 == v2)
print("v2 == v3:", v2 == v3)

print()

print("v1 < v2:", v1 < v2)
print("v1 < v3:", v1 < v4)
print("v2 < v3:", v2 < v3)
print("v2 < v4:", v2 < v4)

print()

print("v1 > v2:", v1 > v2)
print("v1 > v4:", v1 > v4)
print("v2 > v4:", v2 > v4)
print("v2 > v1:", v2 > v1)
