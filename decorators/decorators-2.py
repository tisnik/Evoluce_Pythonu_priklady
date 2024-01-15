# Transformace funkce s využitím dekorátorů:
# - tisk argumentů původní funkce
# - tisk návratové hodnoty původní funkce

def print_params_and_return_val(function):
    """Transformace předané funkce."""

    def wrapper(x, y):
        """Nová funkce volající předanou funkci."""
        print(f"Arguments: x={x} y={y}")
        value = function(x, y)
        print(f"Computed value: {value}")
        return value

    # vrátit novou funkci
    return wrapper


@print_params_and_return_val
def add(a, b):
    return a+b


# toto již není původní funkce!
add(1, 2)

print()

# toto již není původní funkce!
add(3, 4)
