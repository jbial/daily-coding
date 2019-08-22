"""
This problem was asked by Google.

Given an undirected graph represented as an adjacency matrix and an integer k,
write a function to determine whether each vertex in the graph can be colored
such that no two adjacent vertices share the same color using at most k colors.

Solution:
Color each vertex with k colors and backtrack over invalid colorations
"""

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def __str__(self):
        return '\n'.join(str(row) for row in self.graph)

    def valid(self, vertex, colors, c):
        """Check whether the color c is valid for a given vertex
        """
        for v in range(self.vertices):
            if self.graph[vertex][v] == 1 and colors[v] == c:
                return False
        return True

    def color_graph(self, k, colors, vertex):
        """Tries all possible colorings for a given vertex
        """
        # all the vertices have been colored
        if vertex == self.vertices:
            return True

        # color every vertex and backtrack if the next vertex is not colorable
        for color in range(1, k + 1):
            if self.valid(vertex, colors, color):
                colors[vertex] = color
                if self.color_graph(k, colors, vertex + 1):
                    return True
                colors[vertex] = 0
        return False

    def k_colorable(self, k):
        """Determines if the graph is k-colorable
        """
        # define a colors array that maps 1-1 with the vertices
        colors = [0 for _ in range(self.vertices)]

        # color the graph starting at the first vertex
        if self.color_graph(k, colors, 0):
            return True
        else:
            return False


def main():

    # test case 1: 4-complete graph
    g1 = Graph(4)
    g1_pts = [(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)]
    for x, y in g1_pts:
        g1.graph[x][y] = 1
        g1.graph[y][x] = 1

    # test case 2: 5-cycle graph
    g2 = Graph(5)
    g2_pts = [(0,1), (0,4), (1,2), (2,3), (3, 4)]
    for x, y in g2_pts:
        g2.graph[x][y] = 1
        g2.graph[y][x] = 1

    # test case 3: 4-wheel graph
    g3 = Graph(5)
    g3_pts = [(0,1), (0,2), (0,3), (1,2), (1,4), (2,3), (2,4), (3, 4)]
    for x, y in g3_pts:
        g3.graph[x][y] = 1
        g3.graph[y][x] = 1

     # (k, colorable) pairs for g1, g2, g3
    test_cases = [ 
        ([2, 3, 4], [False, False, True]),  
        ([2, 3, 4], [False, True, True]),
        ([2, 3, 4], [False, True, True])
    ]

    if all([
        all([g.k_colorable(k) == ans for k, ans in zip(*test)])
        for test, g in zip(test_cases, [g1, g2, g3])]):
        print("Passed")
    else:
        print("Failed")


if __name__ == '__main__':
    main()



