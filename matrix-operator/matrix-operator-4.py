# Operátor maticového násobení:
# - přetížení operátoru @= kombinujícího maticové násobení s přiřazením


class Test:
    """Třída s přetíženým operátorem @=."""

    def __init__(self, x):
        """Konstruktor."""
        self.value = str(x)

    def __str__(self):
        """Metoda volaná při tisku objektu."""
        return self.value

    def __imatmul__(self, other):
        """Metoda přetěžující operátor @=."""
        self.value = f"({self.value} @ {other.value})"
        return self


# konstrukce několika instancí třídy Test
t1 = Test(1)
print("t1:", t1)

t2 = Test(2)
print("t2:", t2)

t3 = Test(3)
print("t3:", t3)

# "maticové násobení" s přiřazením
t3 @= t1
print("t3 @= t1:", t3)

# "maticové násobení" s přiřazením
t3 @= t2
print("t3 @= t2:", t3)
