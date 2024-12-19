# Python3 program to find whether a
# universal sink exists in a directed graph
class Graph:

    # constructor to initialize number of
    # vertices and size of adjacency matrix
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_matrix = [[0 for i in range(vertices)]
                                 for j in range(vertices)]

    def insert(self, s, destination):

        # make adjacency_matrix[i][j] = 1
        # if there is an edge from i to j
        self.adjacency_matrix[s - 1][destination - 1] = 1

    def issink(self, i):
        for j in range(self.vertices):

            # if any element in the row i is 1, it means
            # that there is an edge emanating from the
            # vertex, which means it cannot be a sink
            if self.adjacency_matrix[i][j] == 1:
                return False

            # if any element other than i in the column
            # i is 0, it means that there is no edge from
            # that vertex to the vertex we are testing
            # and hence it cannot be a sink
            if self.adjacency_matrix[j][i] == 0 and j != i:
                return False

        # if none of the checks fails, return true
        return True

    # we will eliminate n-1 non sink vertices so that
    # we have to check for only one vertex instead of
    # all n vertices
    def eliminate(self):
        i = 0
        j = 0
        while i < self.vertices and j < self.vertices:

            # If the index is 1, increment the row
            # we are checking by 1
            # else increment the column
            if self.adjacency_matrix[i][j] == 1:
                i += 1
            else:
                j += 1

        # If i exceeds the number of vertices, it
        # means that there is no valid vertex in
        # the given vertices that can be a sink
        if i > self.vertices:
            return -1
        elif self.issink(i) is False:
            return -1
        else:
            return i


# Driver Code
if __name__ == "__main__":

    number_of_vertices = 6
    number_of_edges = 5
    g = Graph(number_of_vertices)

    # input set 1
    # g.insert(1, 6)
    # g.insert(2, 6)
    # g.insert(3, 6)
    # g.insert(4, 6)
    # g.insert(5, 6)

    # input set 2
    g.insert(1, 6)
    g.insert(2, 3)
    g.insert(2, 4)
    g.insert(4, 3)
    g.insert(5, 3)

    vertex = g.eliminate()

    # returns 0 based indexing of vertex.
    # returns -1 if no sink exits.
    # returns the vertex number-1 if sink is found
    if vertex >= 0:
        print("Sink found at vertex %d" % (vertex + 1))
    else:
        print("No Sink")
