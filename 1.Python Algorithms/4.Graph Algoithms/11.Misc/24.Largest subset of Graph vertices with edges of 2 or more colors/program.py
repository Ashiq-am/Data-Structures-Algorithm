# Python3 program to find size of subset
# of graph vertex such that each vertex
# has more than 1 color edges

# function to calculate max subset size
def subsetGraph(C):
    global N

    # set for number of vertices
    vertices = set()
    for i in range(N):
        vertices.add(i)

    # loop for deletion of vertex from set
    while (len(vertices) != 0):

        # if subset has only 1 vertex return 0
        if (len(vertices) == 1):
            return 1

        # for each vertex iterate and keep removing
        # a vertix while we find a vertex with all
        # edges of same color.
        someone_removed = False
        for x in vertices:

            # note down different color values
            # for each vertex
            values = set()
            for y in vertices:
                if (y != x):
                    values.add(C[x][y])

            # if only one color is found
            # erase that vertex (bad vertex)
            if (len(values) == 1):
                vertices.remove(x)
                someone_removed = True
                break

        # If no vertex was removed in the
        # above loop.
        if (not someone_removed):
            break

    return len(vertices)


# Driver Code

# Number of vertices
N = 6
C = [[0, 9, 2, 4, 7, 8],
     [9, 0, 9, 9, 7, 9],
     [2, 9, 0, 3, 7, 6],
     [4, 9, 3, 0, 7, 1],
     [7, 7, 7, 7, 0, 7],
     [8, 9, 6, 1, 7, 0]]
print(subsetGraph(C))
