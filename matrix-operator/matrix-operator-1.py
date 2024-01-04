# Operátor maticového násobení:
# - přetížení operátoru maticového násobení @


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


# konstrukce několika instancí třídy Test
t1 = Test(1)
print("t1:", t1)

t2 = Test(2)
print("t2:", t2)

t3 = Test(3)
print("t3:", t3)

# použití přetíženého operátoru
t4 = t1 @ t2
print("t1 @ t2:", t4)

# test asociativity
t5 = t1 @ t2 @ t3
print("t1 @ t2 @ t3:", t5)

# test změny priority operací pomocí závorek
t6 = t1 @ (t2 @ t3)
print("t1 @ (t2 @ t3):", t6)

t7 = t1 @ t5
print("t1 @ t5:", t7)
