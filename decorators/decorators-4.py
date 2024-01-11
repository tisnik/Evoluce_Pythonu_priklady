# Transformace funkce s využitím dekorátoru:
# - problematika rekurzivní funkce


def print_operation_params_and_return_val(name):

    def decorate(fn):
        """Transformace předané funkce."""
        def wrapper(x, y):
            """Nová funkce volající předanou funkci."""
            print(f"Parameters for computing {name}: x={x} y={y}")
            value = fn(x, y)
            print(f"Computed value: {value}")
            return value
        return wrapper

    # vrátit novou funkci
    return decorate
    """Transformace předané funkce."""


@print_operation_params_and_return_val(name="Ackermann")
def A(m, n):
    """Ackermannova funkce, která je rekurzivní."""
    if m == 0:
        return n + 1
    if n == 0:
        return A(m - 1, 1)
    return A(m - 1, A(m, n - 1))


# použití obalené rekurzivní funkce
print(A(2, 2))
