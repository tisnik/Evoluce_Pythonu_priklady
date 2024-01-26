# Základy funkcionálního programování v Pythonu:
# - využití standardní funkce vyššího řádu "filter"

# vygenerovat sekvenci celočíselných hodnot
data = range(0, 11)

# získat pouze liché hodnoty ze sekvence
filtered = filter(lambda value: value % 2 == 1, data)
print(list(filtered))

# získat pouze sudé hodnoty ze sekvence
filtered = filter(lambda value: value % 2 == 0, data)
print(list(filtered))
