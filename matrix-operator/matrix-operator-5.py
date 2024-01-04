# Operátor maticového násobení:
# - přetížení operátoru maticového násobení @
# - přetížení operátoru @= kombinujícího maticové násobení s přiřazením


class Test:
    """Třída s přetíženými operátory @ a @=."""

    def __init__(self, x):
        """Konstruktor."""
        self.value = str(x)

    def __str__(self):
        """Metoda volaná při tisku objektu."""
        return self.value

    def __matmul__(self, other):
        """Metoda přetěžující operátor @."""
        return Test(f"({self.value} @ {other.value})")

    def __imatmul__(self, other):
        """Metoda přetěžující operátor @=."""
        return Test(f"({self.value} @ {other.value})")


# konstrukce několika instancí třídy Test
t1 = Test(1)
print("t1:", t1)

t2 = Test(2)
print("t2:", t2)

t3 = Test(3)
print("t3:", t3)

# použití obou přetížených operátorů ve stejném příkazu
t3 @= t1 @ t2
print("t3 @= t1 @ t2:", t3)
