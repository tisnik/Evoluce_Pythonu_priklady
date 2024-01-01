# Základy funkcionálního programování v Pythonu:
# - generátorová notace nahrazující funkci vyššího řádu "filter"

# vygenerovat sekvenci celočíselných hodnot
data = range(0, 11)

# získat pouze liché hodnoty ze sekvence
filtered = [value for value in data if value %2 == 1]
print(filtered)

# získat pouze sudé hodnoty ze sekvence
filtered = [value for value in data if value %2 == 0]
print(filtered)
