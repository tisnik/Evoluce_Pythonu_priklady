# Skupiny výjimek v jazyku Python:
# - skupina výjimek je chápána jako další typ výjimky


# konstrukce skupiny výjimek
eg = ExceptionGroup(
        "Very serious exception",
        [
            TypeError("Unexpected type detected, expecting integer"),
            ExceptionGroup(
                "First sub-group",
                [ValueError("Invalid value"),
                 FileNotFoundError("Can not find file named foo.bar"),
                 ZeroDivisionError("Divided by zero")],
            ),
            ExceptionGroup(
                "Second sub-group",
                [TypeError("Unexpected type detected again, expecting integer"),
                 ZeroDivisionError("Divided by zero")],
            ),
        ],
)

# skupina výjimek je chápána jako další typ výjimky
try:
    print("Let's raise exception group")
    raise eg
except ExceptionGroup as ex:
    print("Caught:", ex)
