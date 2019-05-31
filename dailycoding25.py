def is_match(string, regex):
    """Checks if string matches regex expression
    """

    # initialize the transition table 
    m, n = len(string), len(regex)
    D = [[False for _ in range(n + 1)] for _ in range(m + 1)]

    # base case: empty string and empty expression
    D[0][0] = True

    # idk
    for j in range(1, n + 1):
        if regex[j - 1] == '*':
            if j - 2 >= 0:
                D[0][j] |= D[0][j - 2]

    # build the transition table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # 1) regex = *
            if regex[j - 1] == '*':
                # 1a) regex = .*
                # 1b) regex matches string
                if regex[j - 2] == '.' or regex[j - 2] == string[i - 1]:
                    D[i][j] |= D[i - 1][j]
                # 1c) ignore regex
                D[i][j] |= D[i][j - 2]

            # 2,3) regex = . or regex matches string
            if regex[j - 1] == '.' or regex[j - 1] == string[i - 1]:
                D[i][j] |= D[i - 1][j - 1]

    return D[-1][-1]


def main():
    
    tests = (
        ("aa", "a*"),
        ("hello", "...*o")
    )

    print([is_match(*t) for t in tests])


if __name__ == '__main__':
    main()
