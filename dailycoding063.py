"""
This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function
that returns whether the word can be found in the matrix by going left-to-right,
or up-to-down.

For example, given the following matrix:
[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost column.
Similarly, given the target word 'MASS', you should return true,
since it's the last row.
"""

def col_contains(words, target, i, j, length):
    """Checks if the target word is contained in the col
    """
    return target == "".join(words[k][j] for k in range(i, length))

def row_contains(words, target, i, j, length):
    """Checks if the target word is contained in the row
    """
    return target == "".join(words[i][k] for k in range(j, length))

def find_word(words, target):
    """Checks if target word exists in the words matrix
    """
    length = len(target)
    n, m = len(words), len(words[0])

    if length > n or length > m:
        return False

    for i in range(length):
        for j in range(length):
            if words[i][j] == target[0]:
                if n - i >= length and col_contains(words, target, i, j, length):
                    return True
                if m - j >= length and row_contains(words, target, i, j, length):
                    return True
    return False


def main():

    words = [
        ['F', 'A', 'C', 'I'],
        ['O', 'B', 'Q', 'P'],
        ['A', 'N', 'O', 'B'],
        ['M', 'A', 'S', 'S']
    ]

    tests = {
        "FOAM": True,
        "MASS": True,
        "AB": True,
        "SOQ": False,
        "SAM": False,
        "NBA": False
    }
    if all(tests[k] == find_word(words, k) for k in tests):
        print("Passed")
    else:
        print("Failed")


if __name__ == '__main__':
    main()

