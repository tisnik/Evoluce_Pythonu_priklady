# Strukturální pattern matching:
# - rozpoznání a zpracování příkazů zadaných uživatelem
# - rozdělení příkazů na jednotlivá slova

def perform_command():
    # získat příkaz od uživatele
    response = input("> ")

    match response.split():
        case ["quit"]:
            return "Quit"
        case ["list", "employees"]:
            return "List employees"
        case ["list", "departments"]:
            return "List departments"
        case ["list", "rooms"]:
            return "List rooms"
        case _:
            return "Wrong command"


print(perform_command())
