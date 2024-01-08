# Operátor "unpack" v Pythonu:
# - výpis typů hodnot vytvářených s využitím operace unpack

# n-tice, seznam a množina
x = *range(5), 5
y = [*range(5), 5]
z = {*range(5), 5}

# tisk obsahu i typu kolekcí
print("x:", x, type(x))
print("y:", y, type(y))
print("z:", z, type(z))
