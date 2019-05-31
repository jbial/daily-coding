"""
This problem was asked by Dropbox.

Conway's Game of Life takes place on an infinite two-dimensional
board of square cells. Each cell is either dead or alive,
and at each tick, the following rules apply:

    - Any live cell with less than two live neighbours dies.
    - Any live cell with two or three live neighbours remains living.
    - Any live cell with more than three live neighbours dies.
    - Any dead cell with exactly three live neighbours becomes a live cell.
    - A cell neighbours another cell if it is horizontally, 
      vertically, or diagonally adjacent.

Implement Conway's Game of Life. It should be able to be initialized
with a starting list of live cell coordinates and the number of
steps it should run for. Once initialized, it should print out the
board at each step. Since it's an infinite board, print out
only the relevant coordinates, i.e. from the top-leftmost live cell
to bottom-rightmost live cell.
"""
import curses
import argparse
import time


class Board:
    def __init__(self, n, iters):
        self.n = n
        self.iters = iters
        self.board = [[0] * self.n for _ in range(self.n)]

    def initialize_board(self, init):
        for coord in init:
            if self.is_valid(coord[0], coord[1]):
                self.board[coord[0]][coord[1]] = 1
            else:
                raise ValueError("Invalid coordinate")

    def is_valid(self, x, y):
        if 0 <= x < self.n and 0 <= y < self.n:
            return True
        else:
            return False

    def counts_live_cells(self, x, y):
        live = 0
        for i, j in [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]:
            if self.is_valid(x + i, y + j):
                live += 1 if self.board[x + i][y + j] else 0
        return live

    def update_board(self):
        switch_on, switch_off = [], []
        for i in range(self.n):
            for j in range(self.n):
                live = self.counts_live_cells(i, j)
                if self.board[i][j] and live < 2:
                    switch_off.append((i, j))
                elif self.board[i][j] and live > 3:
                    switch_off.append((i, j))
                elif self.board[i][j] == 0 and live == 3:
                    switch_on.append((i, j))
        
        # apply the updates
        for i, j in switch_off:
            self.board[i][j] = 0
        for i, j in switch_on:
            self.board[i][j] = 1

    def get_board_str(self):
        board_repr = ""
        for i in range(self.n):
            board_repr += " ".join("*" if self.board[i][j] else " " 
                                   for j in range(self.n))
            board_repr += '\n'
        return board_repr

    def simulate(self):
        window = curses.initscr()
        curses.noecho()
        for i in range(self.iters):
            try:
                window.addstr(0, 0, self.get_board_str())
            except curses.error:
                print("Terminal window not large enough for board size")
            self.update_board()
            window.refresh()
            time.sleep(0.01)
        curses.endwin()


def main():
    
    parser = argparse.ArgumentParser(
        description="Ensure size of terminal window can accomodate the \
                     size of the game of life board."
    )
    parser.add_argument("--size", type=int, help="Window size")
    parser.add_argument("--iters", type=int, help="Number of iterations")
    parser.add_argument("--inits", type=str, help="Initial pts: '(a,b) (c,d) ...'")
    args = parser.parse_args()

    if args.iters and args.inits and args.size:
        iters = args.iters
        inits = [[int(i) for i in p.strip("()").split(',')] 
                 for p in args.inits.split()]
        print(inits)
        n = args.size

        b = Board(n, iters)
        b.initialize_board(inits)
        b.simulate()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
