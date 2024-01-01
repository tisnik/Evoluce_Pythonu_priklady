# Základy funkcionálního programování v Pythonu:
# - generátorová notace nahrazující funkci vyššího řádu "filter"


def odd(value):
    """Test, zda je vstupní hodnota lichá."""
    return value % 2 == 1


def even(value):
    """Test, zda je vstupní hodnota sudá."""
    return not odd(value)


# vygenerovat sekvenci celočíselných hodnot
data = range(0, 11)

# získat pouze liché hodnoty ze sekvence
filtered = [value for value in data if odd(value)]
print(filtered)

# získat pouze sudé hodnoty ze sekvence
filtered = [value for value in data if even(value)]
print(filtered)
