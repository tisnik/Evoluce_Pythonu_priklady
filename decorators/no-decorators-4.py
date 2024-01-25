# Transformace funkce bez využití dekorátorů:
# - tisk doby trvání výpočtu

from time import perf_counter


def timer(function):
    """Transformace předané funkce."""

    def wrapper(x, y):
        """Nová funkce volající předanou funkci."""
        t1 = perf_counter()
        value = function(x, y)
        t2 = perf_counter()
        print(f"Elapsed time: {t2-t1}s")
        return value

    # vrátit novou funkci
    return wrapper


def A(m, n):
    """Ackermannova funkce."""
    if m == 0:
        return n + 1
    if n == 0:
        return A(m - 1, 1)
    return A(m - 1, A(m, n - 1))


# transformace (obalení) funkce A
wrapped_a = timer(A)

print(wrapped_a(1, 1))
print(wrapped_a(2, 2))
print(wrapped_a(3, 3))
print(wrapped_a(3, 4))
print(wrapped_a(3, 6))
