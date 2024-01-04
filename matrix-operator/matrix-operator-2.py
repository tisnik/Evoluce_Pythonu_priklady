# Operátor maticového násobení:
# - přetížení operátoru maticového násobení @ pro pravý operand


class Test:
    """Třída s přetíženým operátorem @."""

    def __init__(self, x):
        """Konstruktor."""
        self.value = str(x)

    def __str__(self):
        """Metoda volaná při tisku objektu."""
        return self.value

    def __rmatmul__(self, other):
        """Metoda přetěžující operátor @ pro pravý operand."""
        return Test(f"({self.value} @ {other})")


# konstrukce instance třídy Test
t1 = Test(1)
print("t1:", t1)

# použití přetíženého operátoru
t2 = "foo" @ t1
print("'foo' @ t1:", t2)

# použití přetíženého operátoru
t3 = "bar" @ t2
print("'bar' @ t2:", t3)
