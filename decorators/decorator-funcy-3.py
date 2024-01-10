# Transformace funkce s využitím dekorátorů:
# - tisk parametrů původní funkce
# - tisk návratové hodnoty původní funkce
# - zkrácený zápis založený na dekorátoru @decorator

from funcy import decorator

@decorator
def print_params_and_return_val(function):
    """Transformace předané funkce."""
    x = function.a
    y = function.b

    print(f"Parameters: x={x} y={y}")
    value = function()
    print(f"Computed value: {value}")
    return value


@print_params_and_return_val
def add(a, b):
    return a+b


# toto již není původní funkce!
add(1, 2)

print()

# toto již není původní funkce!
add(3, 4)
