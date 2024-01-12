# Formátovací řetězce v Pythonu:
# - výpis tabulky, jejíž jeden sloupec obsahuje hodnoty
#   vypsané formou procent

# výpis obsahu řetězce po doplnění hodnot dle šablony
print(f"{'částka' : >5} {'úrok' : >5} {'za rok' : >7} {'za 5 let' : >7}")

castka = 1000

for i in range(1, 11):
    urok = i / 10.0
    za_rok = castka * (1+urok)
    za_5_let = castka * (1+urok)**5
    # výpis obsahu řetězce po doplnění hodnot dle šablony
    print(f"{castka : >5} {urok : 5.0%} {za_rok : >7.0f} {za_5_let : > 7.0f}")
