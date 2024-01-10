# Transformace funkce s využitím dekorátoru:
# - obalení funkce voláním dalších příkazů
# - vliv pořadí dekorátorů na výsledek
# - zkrácený zápis založený na dekorátoru @decorator

from funcy import decorator


@decorator
def simple_dashes(function):
    """Transformace předané funkce."""
    print("-" * 40)
    function()
    print("-" * 40)


@decorator
def double_dashes(function):
    """Transformace předané funkce."""
    print("=" * 40)
    function()
    print("=" * 40)


@simple_dashes
@double_dashes
def hello():
    print("Hello!")


# zavolat dvakrát obalenou funkci
hello()
