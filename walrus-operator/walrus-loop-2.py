# Mroží operátor v Pythonu:
# - programová smyčka typu while založená
#   na použití mrožího operátoru

# otevření souboru pro čtení
with open("test.txt", "r") as f:
    # přečtení všech řádků ze souboru
    while line := f.readline():
        print(line.strip())
