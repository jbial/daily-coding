"""
This problem was asked by Facebook.

There is an N by M matrix of zeroes. Given N and M, write a function
to count the number of ways of starting at the top-left corner and
getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are
two ways to get to the bottom-right:

Right, then down
Down, then right

Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

Solution:

"""

def count_paths_rec(i, j, n, m):
    if i == n - 1 and j == m - 1: 
        return 1
    elif i > n - 1 or j > m - 1:
        return 0

    return count_paths_rec(i + 1, j, n, m) + count_paths_rec(i, j + 1, n, m)


def count_paths(n, m):
    if not n or not m:
        return None
    return count_paths_rec(0, 0, n, m)


def main():

    tests = {
        (1, 1): 1,
        (2, 2): 2,
        (3, 3): 6,
        (4, 4): 20,
        (5, 5): 70,
        (4, 3): 10,
        (9, 0): None,
        (3, 2): 3
    }

    if all(tests[k] == count_paths(*k) for k in tests):
        print("Passed")
    else:
        print("Failed")


if __name__ == '__main__':
    main()

