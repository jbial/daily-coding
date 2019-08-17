class Point:
    def __init__(self, a, b, dist=0):
        self.x = a
        self.y = b
        self.dist = dist


def is_valid(grid, visited, x, y):
    """Check if given point is valid on the grid
    - coordinate is within grid
    - coordinate has not been visited
    - coordinate is not a wall coord
    """
    return (0 <= x) and (x < len(grid[0])) and (0 <= y) and (y < len(grid)) \
        and grid[x][y] == 0 and not visited[x][y]


def check_window(grid, visited, prev_dist, x, y):
    """iterator for the valid maze points
    - checks the left, right, up, down coords
    """
    for i, j in ([-1, 0], [0, 1], [1, 0], [0, -1]):
        if is_valid(grid, visited, x + i, y + j):
            visited[x + i][y + j] = True
            yield Point(x + i, y + j, prev_dist + 1)


def shortest_path(grid, start, end):
    """Return length of shortest path using BFS
    """
    queue = []
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]

    # Initialize by pushing start coord to queue
    queue.insert(0, start)
    visited[start.x][start.y] = True

    # Loop until current node has the same coordinates as the end
    while queue:

        # Get the first node from the queue
        node = queue[-1]
        queue.pop()
        x, y, dist = node.x, node.y, node.dist

        if x == end.x and y == end.y:
            return dist

        # Add all valid neighbors to the queue
        for v_node in check_window(grid, visited, dist, x, y):
            queue.insert(0, v_node)

    # Shortest path not possible
    return -1


def main():
    """Shortest path finder using Lee algorithm
    """
    mazes = (
        [[
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0]
        ], Point(3, 0), Point(0, 3)],
        [[
            [0, 0, 0, 0],
            [0, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ], Point(0, 2), Point(3, 2)],
        [[
            [0, 0, 1, 0],
            [1, 0, 0, 1],
            [0, 1, 0, 0],
            [0, 0, 0, 0]
        ], Point(3, 0), Point(0, 0)],
        [[
            [1, 0, 0, 0],
            [1, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]
        ], Point(3, 0), Point(1, 1)],
        [[
            [0, 0, 0, 0],
            [1, 0, 1, 1],
            [0, 1, 0, 0],
            [0, 0, 0, 0]
        ], Point(0, 0), Point(0, 0)],
        [[
            [0, 0, 0, 0],
            [1, 0, 1, 1],
            [0, 1, 0, 0],
            [0, 0, 0, 0]
        ], Point(3, 0), Point(0, 0)]
    )
    maze_paths = (6, 7, 7, 9, 0, -1)
    if all([shortest_path(*test) == ans for test, ans in zip(mazes, maze_paths)]):
        print("Passed")
    else:
        print("Failed")
    import numpy as np
    a = np.


if __name__ == '__main__':
    main()
