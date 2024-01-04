# Uzávěry:
# - modifikace lokální proměnné obsahující referenci na funkci


def foo():

   def bar():
       """První varianta funkce bar()."""
       print("original BAR")

   def other_bar():
       """Druhá varianta funkce bar()."""
       print("modified BAR")

   def baz(modify):
       """Modifikace lokální funkce bar."""
       # budeme modifikovat nelokální proměnnou bar
       nonlocal bar
       if modify:
           bar = other_bar
       return bar

   # vrátit uzávěr, který nám umožní volat funkci baz
   return baz


x = foo()

print(x)
x(False)()
x(True)()
