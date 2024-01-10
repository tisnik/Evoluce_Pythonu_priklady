# Mroží operátor v Pythonu:
# - lokální proměnná result je viditelná
#   i po konstrukci seznamu s výsledky.

def A(m, n):
    """Ackermannova funkce."""
    if m == 0:
        return n + 1
    if n == 0:
        return A(m - 1, 1)
    return A(m - 1, A(m, n - 1))


results = [result for m in range(4) for n in range(7) if (result := A(m, n)) %2 != 0]

# zobrazení vypočtených výsledků
print(results)

# existuje proměnná result?
print(result)
