# Python Program to check
# if there is a
# negative weight
# cycle using Floyd
# Warshall Algorithm


# Number of vertices
# in the graph
V = 4

# Define Infinite as a
# large enough value. This
# value will be used
# for vertices not connected
# to each other
INF = 99999


# Returns true if graph has
# negative weight cycle
# else false.
def negCyclefloydWarshall(graph):
    # dist[][] will be the
    # output matrix that will
    # finally have the shortest
    # distances between every
    # pair of vertices
    dist = [[0 for i in range(V + 1)] for j in range(V + 1)]

    # Initialize the solution
    # matrix same as input
    # graph matrix. Or we can
    # say the initial values
    # of shortest distances
    # are based on shortest
    # paths considering no
    # intermediate vertex.
    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]

    ''' Add all vertices one
        by one to the set of
        intermediate vertices.
    ---> Before start of a iteration,
        we have shortest
        distances between all pairs
        of vertices such
        that the shortest distances
        consider only the
        vertices in set {0, 1, 2, .. k-1}
        as intermediate vertices.
    ----> After the end of a iteration,
        vertex no. k is
        added to the set of
        intermediate vertices and
        the set becomes {0, 1, 2, .. k} '''
    for k in range(V):

        # Pick all vertices
        # as source one by one
        for i in range(V):

            # Pick all vertices as
            # destination for the
            # above picked source
            for j in range(V):

                # If vertex k is on
                # the shortest path from
                # i to j, then update
                # the value of dist[i][j]
                if (dist[i][k] + dist[k][j] < dist[i][j]):
                    dist[i][j] = dist[i][k] + dist[k][j]

    # If distance of any
    # vertex from itself
    # becomes negative, then
    # there is a negative
    # weight cycle.
    for i in range(V):
        if (dist[i][i] < 0):
            return True

    return False


# Driver code


''' Let us create the
	following weighted graph
			1
	(0)----------->(1)
	/|\			 |
	|			 |
-1 |			 | -1
	|			 \|/
	(3)<-----------(2)
		-1	 '''

graph = [[0, 1, INF, INF],
         [INF, 0, -1, INF],
         [INF, INF, 0, -1],
         [-1, INF, INF, 0]]

if (negCyclefloydWarshall(graph)):
    print("Yes")
else:
    print("No")
