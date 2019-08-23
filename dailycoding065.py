"""
This problem was asked by Amazon.

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:

1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12

Solution:
Print each row/col in a clockwise manner, decrementing/incrementing the row/col
index to print until
"""

def print_spiral(arr):

    # indices of the row and columns to begin printing from
    last_row, last_col = len(arr), len(arr[0])
    first_row = first_col = 0

    while first_row < last_row and first_col < last_col:

        # print left to right row
        for j in range(last_col):
            print(arr[first_row][j], end=" ")
        first_row += 1

        # print top to bottom col
        for i in range(first_row, last_row):
            print(arr[i][last_col - 1], end=" ")
        last_col -= 1

        # print right to left row
        if first_row < last_row:
            for j in range(last_col - 1, first_col - 1, -1):
                print(arr[last_row - 1][j], end=" ")
            last_row -= 1

        # print bottom to top col
        if first_col < last_col:
            for i in range(last_row - 1, first_row, -1):
                print(arr[i][first_col], end=" ")
            first_col += 1

    # print empty line
    print()


def main():
    
    test1 = [[1,  2,  3,  4,  5],
            [6,  7,  8,  9,  10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]]


    test2 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12],
            [13, 14, 15]]

    def print_arr(arr):
        for row in arr:
            print(row)
        print()

    print("Test 1: ")
    print_arr(test1)
    print("Spiral Test 1: ")
    print_spiral(test1)
    print()

    print("Test 2: ")
    print_arr(test2)
    print("Spiral Test 2: ")
    print_spiral(test2)

    print("\nPassed")


if __name__ == '__main__':
    main()

