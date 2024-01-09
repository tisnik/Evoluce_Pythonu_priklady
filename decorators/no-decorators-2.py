# Transformace funkce bez využití dekorátorů:
# - tisk parametrů původní funkce
# - tisk návratové hodnoty původní funkce

def print_params_and_return_val(function):
    """Transformace předané funkce."""

    def wrapper(x, y):
        """Nová funkce volající předanou funkci."""
        print(f"Parameters: x={x} y={y}")
        value = function(x, y)
        print(f"Computed value: {value}")
        return value

    # vrátit novou funkci
    return wrapper


def add(a, b):
    return a+b


# transformace (obalení) funkce add
wrapped_add = print_params_and_return_val(add)

print("Original add:\n")
add(1, 2)

print("\n\nWrapped add:\n")
wrapped_add(1, 2)
