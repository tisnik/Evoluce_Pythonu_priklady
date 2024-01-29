# Typové anotace a nástroj Mypy:
# - funkce append s typovými anotacemi
# - korektní řešení (z pohledu typového systému)


def append(a: str, b: str) -> str:
    return a.strip() + b.strip()
