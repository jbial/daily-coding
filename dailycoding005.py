def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    def first(a, b):
        return a
    return pair(first)


def cdr(pair):
    def second(a, b):
        return b
    return pair(second)


def main():

    pair = cons(4324, 5435)
    print("Passed" if car(pair) == 4324 and cdr(pair) == 5435 else "Failed")


if __name__ == '__main__':
    main()
