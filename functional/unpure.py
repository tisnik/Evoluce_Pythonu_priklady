# Základy funkcionálního programování v Pythonu:
# - ukázka "nečisté" funkce

lst = []


def unpure(item):
    lst.append(item)


unpure("foo")
unpure("bar")
unpure("baz")

print(lst)
