# Mroží operátor v Pythonu:
# - dvojí volání funkcí len() a sum()

values = (1, 2, 3, 4, 5)

result = {
    "count": len(values),
    "sum": sum(values),
    "mean": sum(values) / len(values),
}

print(result)
