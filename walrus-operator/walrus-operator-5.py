# Mroží operátor v Pythonu:
# - volání funkcí len() a sum() pouze jedenkrát,
# - použití pomocných proměnných na globální úrovni

values = (1, 2, 3, 4, 5)

count = len(values)
summ = sum(values)

result = {
    "count": count,
    "sum": summ,
    "mean": summ / count,
}

print(result)
