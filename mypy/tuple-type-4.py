# Typové anotace a nástroj Mypy:
# - definice n-tice se čtyřmi prvky různých typů
# - kompatibilita s Mypy

from typing import Tuple

p: Tuple[int, float, bool, str] = (2.0, 3.14, 1, "Hello")
