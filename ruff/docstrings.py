"""Ukázka přetížení operátoru @."""

class Test:
    """Třída s přetíženým operátorem @."""

    def __init__(self, x):
        """Konstruktor."""
        self.value = str(x)

    def __str__(self):
        """Metoda volaná při tisku objektu."""
        return self.value

    def __matmul__(self, other):
        """Metoda přetěžující operátor @."""
        return Test(f"({self.value} @ {other.value})")


def test():
    """Test chování třídy s přetíženým operátorem @."""
    t1 = Test(1)
    print("t1:", t1)

    t2 = Test(2)
    print("t2:", t2)

    t3 = t1 @ t2
    print("t1 @ t2:", t3)


test()
