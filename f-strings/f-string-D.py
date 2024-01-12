# Formátovací řetězce v Pythonu:
# - výpis celočíselných hodnot 64 až 95 decimálně, binárně,
#   v osmičkové soustavě, v hexadecimální soustavě a taktéž
#   formou ASCII znaku

# výpis obsahu řetězce po doplnění hodnot dle šablony
print(f"{'DEC'}  {'BIN' : ^7}  {'OCT' : >3}  {'hex' : >2} {'HEX' : >2} {'ASCII'}")

for i in range(64, 64+32):
    # výpis obsahu řetězce po doplnění hodnot dle šablony
    print(f"{i : >2d}  {i : 07b}  {i : >3o}  {i : >2x}  {i : >2X}  {i : >c}")
