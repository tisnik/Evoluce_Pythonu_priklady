# Transformace funkce s využitím dvojice dekorátorů:
# - vliv pořadí dekorátorů na výsledek

def simple_dashes(function):
    """Transformace předané funkce."""

    def wrapper():
        """Nová funkce volající předanou funkci."""
        print("-" * 40)
        function()
        print("-" * 40)

    # vrátit novou funkci
    return wrapper


def double_dashes(function):
    """Transformace předané funkce."""

    def wrapper():
        """Nová funkce volající předanou funkci."""
        print("=" * 40)
        function()
        print("=" * 40)

    # vrátit novou funkci
    return wrapper


@simple_dashes
@double_dashes
def hello():
    print("Hello!")


# zavolat dvakrát obalenou funkci
hello()
