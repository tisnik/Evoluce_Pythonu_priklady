# Výpis hodnot vytvářených s využitím operace unpack

d = {"x": 1,
     "y": 2,
     "z": 3}

# rozbalení slovníku
x = {**d, "a": 10, "b": 20}
print(x)
