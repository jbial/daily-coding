"""
This problem was asked by Dropbox.

Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid
with digits. The objective is to fill the grid with the constraint that
every row, column, and box (3 by 3 subgrid) must contain all of
the digits from 1 to 9.

Implement an efficient sudoku solver.
"""

def init_board(init_points):
    board = [[0] * 9 for _ in range(9)]

    for (x, y), val in init_points.items():
        board[x][y] = val
    return board


def _is_complete(board):
    return all(all(val != 0 for val in row) for row in board)


def _find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def _duplicates(arr):
    vals = dict()
    for val in arr:
        if val in vals and val != 0:
            return True
        vals[val] = True
    return False


def _rows_valid(board):
    for row in board:
        if _duplicates(row):
            return False
    return True


def _cols_valid(board):
    for i in range(9):
        if _duplicates([board[j][i] for j in range(9)]):
            return False
    return True


def _block_valid(board):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if _duplicates([board[i+k][j+l] for l in range(3) for k in range(3)]):
                return False
    return True


def board_valid(board):
    return _rows_valid(board) and _cols_valid(board) and _block_valid(board)


def solve(board):
    if _is_complete(board):
        return board

    i, j = _find_empty_cell(board)
    for n in range(1, 10):
        board[i][j] = n
        if board_valid(board):
            result = solve(board)
            if _is_complete(result):
                return result
        board[i][j] = 0
    return board


def print_board(board):
    for row in board:
        print(row)


def main():
    
    import random

    init_pts = {tuple(random.sample(range(9), 2)): i for i in range(1, 10)}
    board = init_board(init_pts)

    print("Initial board:")
    print_board(board)

    board = solve(board)
    
    print("\nSolved board:")
    print_board(board)

    if _is_complete(board) and board_valid(board):
        print("\nPassed")
    else:
        print("\nFailed")


if __name__ == '__main__':
    main()
