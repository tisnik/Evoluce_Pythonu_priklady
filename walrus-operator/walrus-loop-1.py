# Mroží operátor v Pythonu:
# - programová smyčka typu while realizovaná
#   bez použití mrožího operátoru

# otevření souboru pro čtení
with open("test.txt", "r") as f:
    # přečtení prvního řádku ze souboru
    line = f.readline()
    # přečtení dalších řádků ze souboru
    while line:
        print(line.strip())
        line = f.readline()
