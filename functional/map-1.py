# Základy funkcionálního programování v Pythonu:
# - využití standardní funkce vyššího řádu "map"

# vstupní zpráva
message = "Lorem ipsum dolor sit amet, consectetur adipiscing " \
          "elit, sed do eiusmod tempor incididunt ut labore et " \
          "dolore magna aliqua"

# rozdělení zprávy na jednotlivá slova
words = message.split()

# výpočet délky všech slov
lengths = map(len, words)

# výpis výsledku
print(list(lengths))
