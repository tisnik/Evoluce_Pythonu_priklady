class Test:
    def __init__(self, x):
        self.value = str(x)

    def __str__(self):
        return self.value

    def __matmul__(self, other):
        return Test(f"({self.value} @ {other.value})")


def test():
    t1 = Test(1)
    print("t1:", t1)

    t2 = Test(2)
    print("t2:", t2)

    t3 = t1 @ t2
    print("t1 @ t2:", t3)


test()
