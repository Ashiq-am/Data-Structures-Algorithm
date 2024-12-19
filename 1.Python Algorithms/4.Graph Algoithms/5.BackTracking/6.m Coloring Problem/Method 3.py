# Python3 program for the above approach
from queue import Queue


class node:
    color = 1
    edges = set()


def canPaint(nodes, n, m):
    # Create a visited array of n
    # nodes, initialized to zero
    visited = [0 for _ in range(n + 1)]

    # maxColors used till now are 1 as
    # all nodes are painted color 1
    maxColors = 1

    # Do a full BFS traversal from
    # all unvisited starting points
    for _ in range(1, n + 1):
        if visited[_]:
            continue

        # If the starting point is unvisited,
        # mark it visited and push it in queue
        visited[_] = 1
        q = Queue()
        q.put(_)

        # BFS Travel starts here
        while not q.empty():
            top = q.get()

            # Checking all adjacent nodes
            # to "top" edge in our queue
            for _ in nodes[top].edges:

                # IMPORTANT: If the color of the
                # adjacent node is same, increase it by 1

                if nodes[top].color == nodes[_].color:
                    nodes[_].color += 1

                # If number of colors used shoots m,
                # return 0
                maxColors = max(maxColors, max(
                    nodes[top].color, nodes[_].color))

                if maxColors > m:
                    print(maxColors)
                    return 0

                # If the adjacent node is not visited,
                # mark it visited and push it in queue
                if not visited[_]:
                    visited[_] = 1
                    q.put(_)

    return 1


# Driver code
if __name__ == "__main__":

    n = 4
    graph = [[0, 1, 1, 1],
             [1, 0, 1, 0],
             [1, 1, 0, 1],
             [1, 0, 1, 0]]

    # Number of colors
    m = 3

    # Create a vector of n+1
    # nodes of type "node"
    # The zeroth position is just
    # dummy (1 to n to be used)
    nodes = []
    for _ in range(n + 1):
        nodes.append(node())

    # Add edges to each node as
    # per given input
    for _ in range(n):
        for __ in range(n):
            if graph[_][__]:
                # Connect the undirected graph
                nodes[_].edges.add(_)
                nodes[__].edges.add(__)

    # Display final answer
    print(canPaint(nodes, n, m))
