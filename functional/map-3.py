# Základy funkcionálního programování v Pythonu:
# - využití standardní funkce vyššího řádu "map"


def sign(value):
    """Na základě předané hodnoty vrací informace o znaménku."""
    if value < 0:
        return "negative"
    elif value > 0:
        return "positive"
    else:
        return "zero"


# sekvence numerických hodnot
values = range(-10, 11)

# získání informací o tom, zda jsou prvky kladné, záporné či nulové
converted = map(sign, values)

# tisk získaných výsledků na více řádků
for c in converted:
    print(c)
