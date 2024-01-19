# Typové anotace a nástroj Mypy:
# - funkce s typovými anotacemi
# - použití typu Optional

from typing import Optional


def message(msg: Optional[str]) -> None:
    """Funkce s typovými anotacemi."""
    if msg:
        print(msg)
    else:
        print("No message!")


message("Ahoj")
message(None)
