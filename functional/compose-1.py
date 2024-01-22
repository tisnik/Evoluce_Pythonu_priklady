# Kompozice funkcí:
# - založeno na knihovně funcy
# - používá se funkce compose

from funcy import compose

# kompozice dvou standardních funkcí
composed = compose(len, str)

# tisk objektu, který jsme získali
print(composed)

# převod celočíselné hodnoty na řetězec
# následovaný výpočtem jeho délky
print(composed(0))
print(composed(42))
print(composed(1000))
print(composed(-1000))
