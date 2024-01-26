# Základy funkcionálního programování v Pythonu:
# - využití standardní funkce vyššího řádu "map"

# sekvence numerických hodnot
values = range(-10, 11)

# získání informací o tom, zda jsou prvky kladné, záporné či nulové
converted = map(
    lambda x: "negative" if x < 0 else "positive" if x > 0 else "zero", values
)

# tisk získaných výsledků na více řádků
for c in converted:
    print(c)
