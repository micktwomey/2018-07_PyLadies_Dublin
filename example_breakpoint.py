def foo(bar):
    ham = {"ham": bar}
    breakpoint()
    return ham


if __name__ == "__main__":
    foo(20)
    foo("ham")
