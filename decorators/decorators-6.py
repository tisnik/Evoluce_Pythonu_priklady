# Transformace funkce s využitím dekorátoru:
# - získání jména transformované funkce


def simple_dashes(function):
    """Transformace předané funkce."""

    def wrapper():
        """Nová funkce volající předanou funkci."""
        print("-" * 40)
        function()
        print("-" * 40)

    return wrapper


@simple_dashes
def hello():
    print("Hello!")


# zavolat obalenou funkci
hello()

# tisk jména funkce
print("function name:", hello.__name__)
