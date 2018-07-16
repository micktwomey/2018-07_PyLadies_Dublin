def funky(name):
    def func(x):
        return f"{name}: {x}"

    return func


def __getattr__(name):
    return funky(name)


def __dir__():
    return ["ham", "spam", "eggs"]
