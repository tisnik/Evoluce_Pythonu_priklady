# Mroží operátor v Pythonu:
# - dvojí vyhodnocení výrazu num * num pro každý prvek
#   ze vstupního seznamu

numbers = [1, 9, 2, 8, 3, 7, 4, 6, 5]

squares = [num * num for num in numbers if num * num < 30]

print(squares)
