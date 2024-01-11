# Transformace funkce s využitím dekorátoru:
# - tisk jména prováděné operace
# - tisk parametrů původní funkce
# - tisk návratové hodnoty původní funkce

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


@print_operation_params_and_return_val("adition")
def add(a, b):
    return a+b


@print_operation_params_and_return_val("division")
def div(a, b):
    return a/b


add(1, 2)
div(1, 2)
