# Mroží operátor v Pythonu:
# - využití mrožího operátoru: výraz num * num se
#   vyhodnotí pro každý prvek jen jedenkrát

numbers = [1, 9, 2, 8, 3, 7, 4, 6, 5]

squares = [squared for num in numbers if (squared := num * num) < 30]

print(squares)
