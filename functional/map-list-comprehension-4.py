# Základy funkcionálního programování v Pythonu:
# - generátorová notace nahrazující funkci vyššího řádu "map"

# sekvence numerických hodnot
values = range(-10, 11)

# získání informací o tom, zda jsou prvky kladné, záporné či nulové
converted = ["negative" if x < 0 else "positive" if x > 0 else "zero"for x in values]

# tisk získaných výsledků na více řádků
for c in converted:
    print(c)
