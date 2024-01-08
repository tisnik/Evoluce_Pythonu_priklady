# Skupiny výjimek v jazyku Python:
# - vytvoření (konstrukce) skupiny výjimek
# - vnořené skupiny výjimek
# - tisk skupiny výjimek

import traceback

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

# tisk skupiny výjimek
traceback.print_exception(eg)
