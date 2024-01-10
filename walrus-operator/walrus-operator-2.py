# Mroží operátor v Pythonu:
# - mroží operátor zapsaný v podmínce

limit = 8

password = "Hello"

if (length := len(password)) < limit:
    print(f"Password should be longer than {length} chars")
