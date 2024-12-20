# Python3 Program to find minimum edge reversal to get
# atleast one path from source to destination

# method adds a directed edge from u to v with weight w
def addEdge(u, v, w):
    global adj
    adj[u].append((v, w))


# Prints shortest paths from src to all other vertices
def shortestPath(src):
    # Create a set to store vertices that are being
    # prerocessed
    setds = {}

    # Create a vector for distances and initialize all
    # distances as infinite (INF)
    dist = [10 ** 18 for i in range(V)]

    # Insert source itself in Set and initialize its
    global adj
    setds[(0, src)] = 1
    dist[src] = 0

    # /* Looping till all shortest distance are finalized

    # then setds will become empty */
    while (len(setds) > 0):

        # The first vertex in Set is the minimum distance
        # vertex, extract it from set.
        tmp = list(setds.keys())[0]
        del setds[tmp]

        # vertex label is stored in second of pair (it
        # has to be done this way to keep the vertices
        # sorted distance (distance must be first item
        # in pair)
        u = tmp[1]

        # 'i' is used to get all adjacent vertices of a vertex
        # list< pair<int, int> >::iterator i;
        for i in adj[u]:

            # Get vertex label and weight of current adjacent
            # of u.
            v = i[0]
            weight = i[1]

            # If there is shorter path to v through u.
            if (dist[v] > dist[u] + weight):

                # /* If distance of v is not INF then it must be in
                #	 our set, so removing it and inserting again
                #	 with updated less distance.
                #	 Note : We extract only those vertices from Set
                #	 for which distance is finalized. So for them,
                #	 we would never reach here. */
                if (dist[v] != 10 ** 18):
                    del setds[(dist[v], v)]

                # Updating distance of v
                dist[v] = dist[u] + weight
                setds[(dist[v], v)] = 1

    return dist


# /* method adds reverse edge of each original edge
# in the graph. It gives reverse edge a weight = 1
# and all original edges a weight of 0. Now, the
# length of the shortest path will give us the answer.
# If shortest path is p: it means we used p reverse
# edges in the shortest path. */
def modelGraphWithEdgeWeight(edge, E, V):
    global adj
    for i in range(E):
        # original edge : weight 0
        addEdge(edge[i][0], edge[i][1], 0)

        # reverse edge : weight 1
        addEdge(edge[i][1], edge[i][0], 1)


# Method returns minimum number of edges to be
# reversed to reach from src to dest
def getMinEdgeReversal(edge, E, V, src, dest):
    # get modified graph with edge weight
    modelGraphWithEdgeWeight(edge, E, V)

    # get shortes path vector
    dist = shortestPath(src)

    # If distance of destination is still INF,
    # not possible
    if (dist[dest] == 10 ** 18):
        return -1
    else:
        return dist[dest]


# Driver code
if __name__ == '__main__':
    V = 7
    edge = [[0, 1], [2, 1], [2, 3], [5, 1], [4, 5], [6, 4], [6, 3]]
    E, adj = len(edge), [[] for i in range(V + 1)]
    minEdgeToReverse = getMinEdgeReversal(edge, E, V, 0, 6)
    if (minEdgeToReverse != -1):
        print(minEdgeToReverse)
    else:
        print("Not possible")


