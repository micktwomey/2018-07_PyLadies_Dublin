def foo(bar):
    ham = {"ham": bar}
    breakpoint()
    return ham


def main():
    foo(20)
    foo("ham")


if __name__ == "__main__":
    main()
