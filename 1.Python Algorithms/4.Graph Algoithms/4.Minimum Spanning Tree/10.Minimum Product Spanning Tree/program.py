# A Python3 program for getting minimum
# product spanning tree The program is
# for adjacency matrix representation
# of the graph
import math

# Number of vertices in the graph
V = 5


# A utility function to find the vertex
# with minimum key value, from the set
# of vertices not yet included in MST
def minKey(key, mstSet):
    # Initialize min value
    min = 10000000
    min_index = 0

    for v in range(V):

        if (mstSet[v] == False and
                key[v] < min):
            min = key[v]
            min_index = v

    return min_index


# A utility function to print the constructed
# MST stored in parent[] and print Minimum
# Obtaiable product
def printMST(parent, n, graph):
    print("Edge Weight")
    minProduct = 1

    for i in range(1, V):
        print("{} - {} {} ".format(parent[i], i,
                                   graph[i][parent[i]]))
        minProduct *= graph[i][parent[i]]

    print("Minimum Obtainable product is {}".format(
        minProduct))


# Function to construct and print MST for
# a graph represented using adjacency
# matrix representation inputGraph is
# sent for printing actual edges and
# logGraph is sent for actual MST
# operations
def primMST(inputGraph, logGraph):
    # Array to store constructed MST
    parent = [0 for i in range(V)]

    # Key values used to pick minimum
    key = [10000000 for i in range(V)]

    # weight edge in cut
    # To represent set of vertices not
    mstSet = [False for i in range(V)]

    # Yet included in MST
    # Always include first 1st vertex in MST

    # Make key 0 so that this vertex is
    key[0] = 0

    # Picked as first vertex

    # First node is always root of MST
    parent[0] = -1

    # The MST will have V vertices
    for count in range(0, V - 1):

        # Pick the minimum key vertex from
        # the set of vertices not yet
        # included in MST
        u = minKey(key, mstSet)

        # Add the picked vertex to the MST Set
        mstSet[u] = True

        # Update key value and parent index
        # of the adjacent vertices of the
        # picked vertex. Consider only those
        # vertices which are not yet
        # included in MST
        for v in range(V):

            # logGraph[u][v] is non zero only
            # for adjacent vertices of m
            # mstSet[v] is false for vertices
            # not yet included in MST. Update
            # the key only if logGraph[u][v] is
            # smaller than key[v]
            if (logGraph[u][v] > 0 and
                    mstSet[v] == False and
                    logGraph[u][v] < key[v]):
                parent[v] = u
                key[v] = logGraph[u][v]

    # Print the constructed MST
    printMST(parent, V, inputGraph)


# Method to get minimum product spanning tree
def minimumProductMST(graph):
    logGraph = [[0 for j in range(V)]
                for i in range(V)]

    # Constructing logGraph from
    # original graph
    for i in range(V):
        for j in range(V):
            if (graph[i][j] > 0):
                logGraph[i][j] = math.log(graph[i][j])
            else:
                logGraph[i][j] = 0

    # Applyting standard Prim's MST algorithm
    # on Log graph.
    primMST(graph, logGraph)


# Driver code
if __name__ == '__main__':
    ''' Let us create the following graph
        2 3
    (0)--(1)--(2)
        | / \ |
    6| 8/ \5 |7
        | /	 \ |
    (3)-------(4)
            9		 '''
    graph = [[0, 2, 0, 6, 0],
             [2, 0, 3, 8, 5],
             [0, 3, 0, 0, 7],
             [6, 8, 0, 0, 9],
             [0, 5, 7, 9, 0], ]

    # Print the solution
    minimumProductMST(graph)
