# Základy funkcionálního programování v Pythonu:
# - využití standardní funkce vyššího řádu "filter"

# vstupní zpráva
message = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing "
    "elit, sed do eiusmod tempor incididunt ut labore et "
    "dolore magna aliqua"
)

# rozdělení zprávy na jednotlivá slova
words = message.split()

# získat zprávy, které jsou delší než čtyři znaky
filtered = filter(lambda word: len(word) > 4, words)
print(list(filtered))

# získat zprávy, které jsou kratší než pět znaků
filtered = filter(lambda word: len(word) <= 4, words)
print(list(filtered))
