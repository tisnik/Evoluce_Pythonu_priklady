# Mroží operátor v Pythonu:
# - volání funkcí len() a sum() pouze jedenkrát,
# - použití mrožího operátoru

values = (1, 2, 3, 4, 5)

result = {
    "count": (count := len(values)),
    "sum": (summ := sum(values)),
    "mean": summ / count,
}

print(result)
