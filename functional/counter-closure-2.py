# Realizace čítače s využitím uzávěru:
# - tato varianta je korektní v Pythonu 2 i v Pythonu 3


def createCounter():
    # proměnná navázaná na funkci čítače
    counter = [0]

    def next():
        # zvýšení hodnoty nelokální proměnné
        counter[0] += 1
        return counter[0]

    # vrácení čítače s navázanou nelokální proměnnou
    return next



# spuštění testů čítačů
def main():
    # vytvoření dvojice nezávislých čítačů
    counter1 = createCounter()
    counter2 = createCounter()

    # použití čítačů - každé jejich zavolání vrátí hodnotu o jedničku vyšší
    for i in range(1,11):
        result1 = counter1()
        result2 = counter2()
        print("Iteration #%d" % i)
        print("    Counter1: %d" % result1)
        print("    Counter2: %d" % result2)


main()
