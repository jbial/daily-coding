"""
This problem was asked by Google.

A knight's tour is a sequence of moves by a knight on a chessboard
such that all squares are visited once.

Given N, write a function to return the number of knight's tours
on an N by N chessboard.

Solution:
Use backtracking, placing every valid move from every square and adding to
the count when all squares are visited. 
Solution from https://www.dailycodingproblem.com/blog/knights-tour/
"""

def is_valid_move(board, n, i, j):
    return 0 <= i < n and 0 <= j < n and board[i][j] == 0


def valid_moves(board, n, i, j):
    directions = [
            (2, 1),
            (1, 2),
            (1, -2),
            (-2, 1),
            (-1, 2),
            (2, -1),
            (-1, -2),
            (-2, -1)
    ]
    moves = [(i + delta_i, j + delta_j) for delta_i, delta_j in directions]
    return [move for move in moves if is_valid_move(board, n, *move)]


def place_moves(board, tour, n):
    if len(tour) == n * n:
        return 1
    
    count = 0
    for i, j in valid_moves(board, n, *tour[-1]):

        # add next valid move to the knights tour 
        # and mark current square as visited
        tour.append((i, j))
        board[i][j] = 1

        count += place_moves(board, tour, n)

        # backtrack
        tour.pop()
        board[i][j] = 0

    return count


def knights_tours(n):
    count = 0
    for i in range(n):
        for j in range(n):
            board = [[0 for _ in range(n)] for _ in range(n)]
            board[i][j] = 1
            count += place_moves(board, [(i, j)], n)
    return count


def main():

    tests = {1: 1, 2: 0, 3: 0, 4: 0}
    if all(tests[k] == knights_tours(k) for k in tests):
        print("Passed")
    else:
        print("Failed")
    

if __name__ == '__main__':
        main()

