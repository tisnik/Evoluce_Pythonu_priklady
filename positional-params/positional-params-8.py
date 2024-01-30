# Poziční a čistě poziční parametry funkcí:
# - definice a volání funkce s jedním čistě pozičním parametrem
#   a se specifikací výchozí hodnoty


# funkce s jedním čistě pozičním parametrem
# a specifikací výchozích hodnot
def foo(x=0, /, y=0, z=0):
    return x + y - z


# volání funkce bez předání argumentů:
# pro x, y, a z se použijí výchozí hodnoty
print(foo())

# volání funkce s předáním jediného argumentu:
# pro y a z se použijí výchozí hodnoty
print(foo(10))

# volání funkce s předáním dvou argumentů:
# pro z se použije výchozí hodnota
print(foo(10, 20))

# volání funkce s předáním všech tří argumentů
print(foo(1, 2, 10))

# druhé dva argumenty lze stále specifikovat i
# se zadáním jména parametru
print(foo(1, z=1, y=2))
