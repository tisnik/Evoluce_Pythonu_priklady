# Transformace funkce s využitím dekorátoru:
# - zachování původního jména transformované funkce

from functools import wraps


def simple_dashes(function):
    """Transformace předané funkce."""

    @wraps(function)
    def wrapper():
        """Nová funkce volající předanou funkci."""
        print("-" * 40)
        function()
        print("-" * 40)

    return wrapper


@simple_dashes
def hello():
    print("Hello!")


# zavolat dvakrát obalenou funkci
hello()

# tisk jména funkce
print("function name:", hello.__name__)
