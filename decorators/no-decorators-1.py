# Transformace funkce bez využití dekorátorů:
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


def hello():
    print("Hello!")


# transformace (obalení) funkce hello
wrapped_hello = wrap_function(hello)

print("Original hello:\n")
hello()

print("\n\nWrapped hello:\n")
wrapped_hello()
