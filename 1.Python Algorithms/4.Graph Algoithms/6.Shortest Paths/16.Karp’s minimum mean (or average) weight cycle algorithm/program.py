# Python3 program to find minimum
# average weight of a cycle in
# connected and directed graph.

# a struct to represent edges
class edge:
    def __init__(self, u, w):
        self.From = u
        self.weight = w


def addedge(u, v, w):
    edges[v].append(edge(u, w))


# calculates the shortest path
def shortestpath(dp):
    # initializing all distances as -1
    for i in range(V + 1):
        for j in range(V):
            dp[i][j] = -1

    # shortest distance From first vertex
    # to in tself consisting of 0 edges
    dp[0][0] = 0

    # filling up the dp table
    for i in range(1, V + 1):
        for j in range(V):
            for k in range(len(edges[j])):
                if (dp[i - 1][edges[j][k].From] != -1):
                    curr_wt = (dp[i - 1][edges[j][k].From] + edges[j][k].weight)
                    if (dp[i][j] == -1):
                        dp[i][j] = curr_wt
                    else:
                        dp[i][j] = min(dp[i][j], curr_wt)


# Returns minimum value of average
# weight of a cycle in graph.
def minAvgWeight():
    dp = [[None] * V for i in range(V + 1)]
    shortestpath(dp)

    # array to store the avg values
    avg = [-1] * V

    # Compute average values for all
    # vertices using weights of
    # shortest paths store in dp.
    for i in range(V):
        if (dp[V][i] != -1):
            for j in range(V):
                if (dp[j][i] != -1):
                    avg[i] = max(avg[i], (dp[V][i] -
                                          dp[j][i]) / (V - j))

    # Find minimum value in avg[]
    result = avg[0]
    for i in range(V):
        if (avg[i] != -1 and avg[i] < result):
            result = avg[i]

    return result


# Driver Code
V = 4

# vector to store edges
edges = [[] for i in range(V)]

addedge(0, 1, 1)
addedge(0, 2, 10)
addedge(1, 2, 3)
addedge(2, 3, 2)
addedge(3, 1, 0)
addedge(3, 0, 8)

print(minAvgWeight())
