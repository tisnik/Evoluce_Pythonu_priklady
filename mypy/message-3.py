# Typové anotace a nástroj Mypy:
# - funkce s typovými anotacemi
# - použití typu Optional
# - zápis pro Python 3.10 a vyšší


def message(msg: str | None) -> None:
    """Funkce s typovými anotacemi."""
    if msg:
        print(msg)
    else:
        print("No message!")


message("Ahoj")
message(None)
