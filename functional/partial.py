# Přibližná podoba funkce vyššího řádu `partial`


def partial(func, /, *args, **keywords):

    def newfunc(*fargs, **fkeywords):
        newkeywords = {**keywords, **fkeywords}
        return func(*args, *fargs, **newkeywords)

    # atributy přidané k funkci
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc
