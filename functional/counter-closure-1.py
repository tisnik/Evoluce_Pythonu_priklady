# Realizace čítače s využitím uzávěru:
# - tato varianta je nekorektní


def create_counter():
    # proměnná navázaná na funkci čítače
    counter = 0

    def next():
        # pokus o zvýšení nelokální proměnné
        counter += 1
        return counter

    # vrácení čítače s navázanou nelokální proměnnou
    return next


# spuštění testů čítačů
def main():
    # vytvoření dvojice nezávislých čítačů
    counter1 = create_counter()
    counter2 = create_counter()

    # použití čítačů - každé jejich zavolání vrátí hodnotu o jedničku vyšší
    for i in range(1, 11):
        result1 = counter1()
        result2 = counter2()
        print("Iteration #%d" % i)
        print("    Counter1: %d" % result1)
        print("    Counter2: %d" % result2)


main()
