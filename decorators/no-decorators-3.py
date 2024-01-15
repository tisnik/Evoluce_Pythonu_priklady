# Transformace funkce bez využití dekorátorů:
# - tisk jména prováděné operace
# - tisk argumentů původní funkce
# - tisk návratové hodnoty původní funkce

def print_operation_params_and_return_val(function, name):
    """Transformace předané funkce."""

    def wrapper(x, y):
        """Nová funkce volající předanou funkci."""
        print(f"Arguments for computing {name}: x={x} y={y}")
        value = function(x, y)
        print(f"Computed value: {value}")
        return value

    # vrátit novou funkci
    return wrapper


def add(a, b):
    return a+b


def div(a, b):
    return a/b


# transformace (obalení) funkce add
wrapped_add = print_operation_params_and_return_val(add, "adition")

print("Wrapped add:\n")
wrapped_add(1, 2)

# transformace (obalení) funkce div
wrapped_div = print_operation_params_and_return_val(div, "division")

print("\n\nWrapped div:\n")
wrapped_div(1, 2)
