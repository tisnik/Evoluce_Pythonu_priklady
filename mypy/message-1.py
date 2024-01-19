# Typové anotace a nástroj Mypy:
# - funkce s typovými anotacemi


def message(msg: str) -> None:
    """Funkce s typovými anotacemi."""
    if msg:
        print(msg)
    else:
        print("No message!")


message("Ahoj")
message(None)
