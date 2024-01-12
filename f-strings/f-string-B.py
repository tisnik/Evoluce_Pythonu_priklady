# Formátovací řetězce v Pythonu:
# - výpis tabulky převrácených hodnot
# - varianta se šířkami sloupců
#   a přesným počtem cifer za desetinnou tečkou

# výpis obsahu řetězce po doplnění hodnot dle šablony
print(f"{'x' : >5}{'1/x' : >5}")

for x in range(1, 11):
    y = 1/x
    # výpis obsahu řetězce po doplnění hodnot dle šablony
    print(f"{x : 5} {y : 5.2f}")
