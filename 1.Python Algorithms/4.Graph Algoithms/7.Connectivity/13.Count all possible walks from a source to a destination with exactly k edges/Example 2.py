# Python3 program to count walks from
# u to v with exactly k edges

# Number of vertices
V = 4


# A Dynamic programming based function
# to count walks from u to v with k edges
def countwalks(graph, u, v, k):
    # Table to be filled up using DP.
    # The value count[i][j][e] will/
    # store count of possible walks
    # from i to j with exactly k edges
    count = [[[0 for k in range(k + 1)]
              for i in range(V)]
             for j in range(V)]

    # Loop for number of edges from 0 to k
    for e in range(0, k + 1):
        for i in range(V):

            # For source
            for j in range(V):
                # For destination

                # Initialize value
                count[i][j][e] = 0

            # From base cases
            if (e == 0 and i == j):
                count[i][j][e] = 1
            if (e == 1 and graph[i][j] != 0):
                count[i][j][e] = 1

            # Go to adjacent only when number
            # of edges is more than 1
            if (e > 1):

                for a in range(V):

                    # Adjacent of i
                    if (graph[i][a] != 0):
                        count[i][j][e] += count[a][j][e - 1]

    return count[u][v][k]


# Driver code
if __name__ == '__main__':
    # Let us create the graph shown
    # in above diagram
    graph = [[0, 1, 1, 1],
             [0, 0, 0, 1],
             [0, 0, 0, 1],
             [0, 0, 0, 0]]

    u = 0
    v = 3
    k = 2

    print(countwalks(graph, u, v, k))


