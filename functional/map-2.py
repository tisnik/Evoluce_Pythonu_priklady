# Základy funkcionálního programování v Pythonu:
# - využití standardní funkce vyššího řádu "map"

# sekvence numerických hodnot
values = range(-10, 11)

# výpočet absolutních hodnot všech prvků ze sekvence
converted = map(abs, values)

# výpis výsledku
print(list(converted))
