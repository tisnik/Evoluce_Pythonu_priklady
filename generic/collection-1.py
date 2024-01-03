# Generické datové typy v Pythonu
# - typové parametry u programátorem vytvořené kolekce

from typing import TypeVar, Generic
from typing import List


T = TypeVar('T')


class Collection(Generic[T]):
    def __init__(self) -> None:
        self.collection : List[T] = []

    def append(self, item: T) -> None:
        self.collection.append(item)

    def get_all(self) -> List[T]:
        return self.collection


c = Collection[int]()
c.append(1)
c.append(2)
print(c.get_all())
