# Typové anotace a nástroj Mypy:
# - definice slovníku
# - specifikace typu klíčů i typu hodnot

from typing import Dict

d: Dict[str, float] = {}

d["foo"] = 1
d["bar"] = 3.14
d[10] = 10
d[42] = "answer"

print(d)
