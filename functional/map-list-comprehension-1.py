# Základy funkcionálního programování v Pythonu:
# - generátorová notace nahrazující funkci vyššího řádu "map"

# vstupní zpráva
message = "Lorem ipsum dolor sit amet, consectetur adipiscing " \
          "elit, sed do eiusmod tempor incididunt ut labore et " \
          "dolore magna aliqua"

# rozdělení zprávy na jednotlivá slova
words = message.split()

# výpočet délky všech slov
lengths = [len(word) for word in words]

# výpis výsledku
print(lengths)
