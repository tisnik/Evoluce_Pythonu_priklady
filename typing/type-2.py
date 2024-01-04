# Použití nového klíčového slova type:
# - deklarace uživatelských datových typů


# definice nových typů
type ID = int
type Name = str
type Surname = str

# nový typ založený na dříve definovaných typech
type User = (ID, Name, Surname)

# využití typu User
u1:User = (42, "Linus", "Torvalds")
print(u1)
