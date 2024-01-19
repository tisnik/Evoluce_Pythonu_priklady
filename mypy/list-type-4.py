# Typové anotace a nástroj Mypy:
# - definice seznamu s prvky typu int
# - inicializace prvků
# - pokus o vložení prvku s nekorektní hodnotou

from typing import List

lst: List[int] = [1, "foo", 3]
