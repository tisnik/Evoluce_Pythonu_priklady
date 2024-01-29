# Typový systém Pythonu:
# - na funkci add() je navázán parametr funkce dummyAdder()


def dummyAdder(delta: int):
    # lokální funkce, kterou vrátíme
    def add(n: int) -> int:
        # přístup k parametru delta předaného vnější funkci
        return delta + n

    return add


# spuštění testů
def main() -> None:
    adder1 = dummyAdder(0)
    adder2 = dummyAdder(42)
    for i in range(1, 11):
        result1 = adder1(i)
        result2 = adder2(i)
        print("Iteration #%d" % i)
        print("    Adder1: %d" % result1)
        print("    Adder2: %d" % result2)


main()
