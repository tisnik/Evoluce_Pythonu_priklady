# Typové anotace a nástroj Mypy:
# - funkce s určením typů parametrů i návratové hodnoty
# - lze provést statickou typovou kontrolu


def positive(x:float) -> bool:
    return x > 0.0


# zavolání s různým typem argumentů
x:bool = positive(0.5)
y:int = positive(42)
z:float = positive(False)
w:str = positive(3)
