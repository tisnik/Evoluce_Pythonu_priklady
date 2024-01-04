# Základy funkcionálního programování v Pythonu:
# - generátorová notace nahrazující funkci vyššího řádu "map"

# sekvence numerických hodnot
values = range(-10, 11)

# výpočet absolutních hodnot všech prvků ze sekvence
converted = [abs(value) for value in values]

# výpis výsledku
print(converted)
