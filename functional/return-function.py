# Základy funkcionálního programování v Pythonu:
# - funkce jako plnohodnotný datový typ:
# - vrácení funkce z jiné funkce příkazem `return`


def foo():
    def bar():
        print("BAR")

    return bar


# zavoláním foo() získáme funkci bar
x = foo()

# tisk získané hodnoty a jejího typu
print(x, type(x))

# funkci bar nyní můžeme spustit: bar()
x()
