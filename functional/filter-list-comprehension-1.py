# Základy funkcionálního programování v Pythonu:
# - generátorová notace nahrazující funkci vyššího řádu "filter"

# vstupní zpráva
message = "Lorem ipsum dolor sit amet, consectetur adipiscing " \
          "elit, sed do eiusmod tempor incididunt ut labore et " \
          "dolore magna aliqua"

# rozdělení zprávy na jednotlivá slova
words = message.split()

# získat zprávy, které jsou delší než čtyři znaky
filtered = [word for word in words if len(word) > 4]
print(list(filtered))

# získat zprávy, které jsou kratší než pět znaků
filtered = [word for word in words if len(word) <= 4]
print(list(filtered))
