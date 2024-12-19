# Python3 program to find min edge reversal
# to make every node reachable from root
import sys


# Method to dfs in tree and populates
# disRev values
def dfs(g, disRev, visit, u):
    # Visit current node
    visit[u] = True
    totalRev = 0

    # Looping over all neighbors
    for i in range(len(g[u])):
        v = g[u][i][0]

        if (not visit[v]):

            # Distance of v will be one more
            # than distance of u
            disRev[v][0] = disRev[u][0] + 1

            # Initialize back edge count same as
            # parent node's count
            disRev[v][1] = disRev[u][1]

            # If there is a reverse edge from u to i,
            # then only update
            if (g[u][i][1]):
                disRev[v][1] = disRev[u][1] + 1
                totalRev += 1

            totalRev += dfs(g, disRev, visit, v)

    # Return total reversal in subtree rooted at u
    return totalRev


# Method prints root and minimum number of
# edge reversal
def printMinEdgeReverseForRootNode(edges, e):
    # Number of nodes are one more than
    # number of edges
    V = e + 1

    # Data structure to store directed tree
    g = [[] for i in range(V)]

    # disRev stores two values - distance
    # and back edge count from root node
    disRev = [[0, 0] for i in range(V)]

    visit = [False for i in range(V)]

    # u, v
    for i in range(e):
        u = edges[i][0]
        v = edges[i][1]

        # Add 0 weight in direction of u to v
        g[u].append([v, 0])

        # Add 1 weight in reverse direction
        g[v].append([u, 1])

    # Initialize all variables
    for i in range(V):
        visit[i] = False
        disRev[i][0] = disRev[i][1] = 0

    root = 0

    # dfs populates disRev data structure and
    # store total reverse edge counts
    totalRev = dfs(g, disRev, visit, root)

    # UnComment below lines to preach node's
    # distance and edge reversal count from root node
    # for (i = 0 i < V i++)
    # {
    #	 cout << i << " : " << disRev[i][0]
    #		 << " " << disRev[i][1] << endl
    # }
    res = sys.maxsize

    # Loop over all nodes to choose
    # minimum edge reversal
    for i in range(V):

        # (reversal in path to i) + (reversal
        # in all other tree parts)
        edgesToRev = ((totalRev - disRev[i][1]) +
                      (disRev[i][0] - disRev[i][1]))

        # Choose minimum among all values
        if (edgesToRev < res):
            res = edgesToRev
            root = i

    # Print the designated root and total
    # edge reversal made
    print(root, res)


# Driver code
if __name__ == '__main__':
    edges = [[0, 1], [2, 1],
             [3, 2], [3, 4],
             [5, 4], [5, 6],
             [7, 6]]

    e = len(edges)

    printMinEdgeReverseForRootNode(edges, e)
