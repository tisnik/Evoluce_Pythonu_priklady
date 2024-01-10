# Transformace funkce s využitím dekorátoru:
# - obalení funkce voláním dalších příkazů
# - zkrácený zápis založený na dekorátoru @decorator

from funcy import decorator


@decorator
def wrap_function(function):
    """Nová funkce volající předanou funkci."""
    print("-" * 40)
    function()
    print("-" * 40)


@wrap_function
def hello():
    print("Hello!")


# toto již není původní funkce, ale funkce obalená!
hello()
