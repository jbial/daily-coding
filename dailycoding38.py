"""
This problem was asked by Microsoft.

You have an N by N board. Write a function that, given N,
returns the number of possible arrangements of the board
where N queens can be placed on the board without threatening each
other, i.e. no two queens share the same row, column, or diagonal.

solution: https://dailycodingproblem.com/blog/an-introduction-to-backtracking/

Use backtracking by attempting to place a queen in one position in one row
and brute forcing all other possible valid positions in the remaining rows,
but backtracking and returning 0 when there is no possible configuration
given the intial placement in the first row.

Run in O(N^2) time since we try N spots for N rows, and O(N) space since
the board is NxN so we only have to store an array with N elements each 
representing the column index

"""
def is_valid(board):
    """Checks if the current board has no threathening queens
    """
    curr_row, curr_col = len(board) - 1, board[-1]
    for row, col in enumerate(board[:-1]):
        diff = abs(curr_col - col)
        if diff == 0 or diff == abs(curr_row - row):
            return False
    return True


def n_queens(n, board=[]):
    """Use backtracking to try every N^2 positions on the board
    """
    if len(board) == n:
        return 1

    count = 0
    for col in range(n):
        board.append(col)
        if is_valid(board):
            count += n_queens(n, board)
        board.pop()
    return count


def main():

  tests = {
    1: 1,
    2: 0,
    3: 0,
    4: 2,
    5: 10,
    6: 4,
    7: 40,
    8: 92,
    9: 352,
    10: 724
  }

  if all(tests[k] == n_queens(k) for k in tests):
    print("Passed")
  else:
    print("Failed")


if __name__ == '__main__':
  main()


