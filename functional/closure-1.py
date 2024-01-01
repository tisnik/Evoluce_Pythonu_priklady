# Uzávěry v Pythonu:
# - vrácení funkce z jiné funkce příkazem `return`
# - vrácená funkce přistupuje k lokální proměnné své vnější funkce


def foo():
    message = "BAR defined in FOO"

    def bar():
        print(message)
    return bar


# zavoláním foo() získáme funkci bar
x = foo()

# tisk získané hodnoty a jejího typu
print(x, type(x))

# funkci bar nyní můžeme spustit: bar()
x()
