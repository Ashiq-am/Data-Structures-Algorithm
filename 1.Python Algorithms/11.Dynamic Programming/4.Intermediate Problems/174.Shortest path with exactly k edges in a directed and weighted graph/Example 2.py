# Dynamic Programming based Python3
# program to find shortest path with

# A Dynamic programming based function
# to find the shortest path from u to v
# with exactly k edges.
def shortestPath(graph, u, v, k):
    global V, INF

    # Table to be filled up using DP. The
    # value sp[i][j][e] will store weight
    # of the shortest path from i to j
    # with exactly k edges
    sp = [[None] * V for i in range(V)]
    for i in range(V):
        for j in range(V):
            sp[i][j] = [None] * (k + 1)

    # Loop for number of edges from 0 to k
    for e in range(k + 1):
        for i in range(V):  # for source
            for j in range(V):  # for destination

                # initialize value
                sp[i][j][e] = INF

                # from base cases
                if (e == 0 and i == j):
                    sp[i][j][e] = 0
                if (e == 1 and graph[i][j] != INF):
                    sp[i][j][e] = graph[i][j]

                # go to adjacent only when number
                # of edges is more than 1
                if (e > 1):
                    for a in range(V):

                        # There should be an edge from
                        # i to a and a should not be
                        # same as either i or j
                        if (graph[i][a] != INF and i != a and
                                j != a and sp[a][j][e - 1] != INF):
                            sp[i][j][e] = min(sp[i][j][e], graph[i][a] +
                                              sp[a][j][e - 1])

    return sp[u][v][k]


# Driver Code

# Define number of vertices in
# the graph and infinite value
V = 4
INF = 999999999999

# Let us create the graph shown
# in above diagram
graph = [[0, 10, 3, 2],
         [INF, 0, INF, 7],
         [INF, INF, 0, 6],
         [INF, INF, INF, 0]]
u = 0
v = 3
k = 2
print("Weight of the shortest path is",
      shortestPath(graph, u, v, k))
