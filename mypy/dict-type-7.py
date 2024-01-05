# Typové anotace a nástroj Mypy:
# - definice slovníku
# - specifikace typu klíčů i typu hodnot
# - pokus o uložení hodnoty None

from typing import Dict

d:Dict[str, float] = {}

d["foo"] = 1
d["bar"] = 3.14
d["baz"] = None

print(d)
