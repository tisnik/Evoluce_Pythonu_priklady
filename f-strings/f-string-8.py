# Formátovací řetězce v Pythonu:
# - specifikace šířky hodnoty
# - specifikace zarovnání hodnoty
# - výpis tabulky s popularitou jmen

jmena = ("Eliška", "Tereza", "Anna", "Adéla", "Natálie", "Hana")
narozeni = (2332, 1900, 1708, 1535, 1386, 287)

# výpis obsahu řetězce po doplnění hodnot dle šablony
print(f"{'Pořadí' : ^10}{'Jméno' : <10}{'Narození' : >10}")

for i, (jmeno, nar) in enumerate(zip(jmena, narozeni)):
    # výpis obsahu řetězce po doplnění hodnot dle šablony
    print(f"{i : ^10}{jmeno : <10}{nar : >10}")
