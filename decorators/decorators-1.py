# Transformace funkce s využitím dekorátoru:
# - obalení funkce voláním dalších příkazů

def wrap_function(function):
    """Transformace předané funkce."""

    def wrapper():
        """Nová funkce volající předanou funkci."""
        print("-" * 40)
        function()
        print("-" * 40)

    # vrátit novou funkci
    return wrapper


@wrap_function
def hello():
    print("Hello!")


# toto již není původní funkce, ale funkce obalená!
hello()
