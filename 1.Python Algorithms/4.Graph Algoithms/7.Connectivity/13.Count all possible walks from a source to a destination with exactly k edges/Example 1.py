# Python3 program to count walks from
# u to v with exactly k edges

# Number of vertices in the graph
V = 4


# A naive recursive function to count
# walks from u to v with k edges
def countwalks(graph, u, v, k):
    # Base cases
    if (k == 0 and u == v):
        return 1
    if (k == 1 and graph[u][v]):
        return 1
    if (k <= 0):
        return 0

    # Initialize result
    count = 0

    # Go to all adjacents of u and recur
    for i in range(0, V):

        # Check if is adjacent of u
        if (graph[u][i] == 1):
            count += countwalks(graph, i, v, k - 1)

    return count


# Driver Code

# Let us create the graph shown in above diagram
graph = [[0, 1, 1, 1, ],
         [0, 0, 0, 1, ],
         [0, 0, 0, 1, ],
         [0, 0, 0, 0]]

u = 0
v = 3
k = 2
print(countwalks(graph, u, v, k))


