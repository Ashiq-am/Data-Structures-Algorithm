# A Python3 program to find same contacts
# in a list of contacts

# Structure for storing contact details.
class contact:
    def __init__(self, field1,
                 field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3


# A utility function to fill entries in
# adjacency matrix representation of graph
def buildGraph(arr, n, mat):
    # Initialize the adjacency matrix
    for i in range(n):
        for j in range(n):
            mat[i][j] = 0

    # Traverse through all contacts
    for i in range(n):

        # Add mat from i to j and vice versa,
        # if possible. Since length of each
        # contact field is at max some constant.
        # (say 30) so body execution of this for
        # loop takes constant time.
        for j in range(i + 1, n):
            if (arr[i].field1 == arr[j].field1 or
                    arr[i].field1 == arr[j].field2 or
                    arr[i].field1 == arr[j].field3 or
                    arr[i].field2 == arr[j].field1 or
                    arr[i].field2 == arr[j].field2 or
                    arr[i].field2 == arr[j].field3 or
                    arr[i].field3 == arr[j].field1 or
                    arr[i].field3 == arr[j].field2 or
                    arr[i].field3 == arr[j].field3):
                mat[i][j] = 1
                mat[j][i] = 1
                break


# A recuesive function to perform DFS
# with vertex i as source
def DFSvisit(i, mat, visited, sol, n):
    visited[i] = True
    sol.append(i)

    for j in range(n):
        if (mat[i][j] and not visited[j]):
            DFSvisit(j, mat, visited, sol, n)


# Finds similar contacrs in an
# array of contacts
def findSameContacts(arr, n):
    # vector for storing the solution
    sol = []

    # Declare 2D adjaceny matrix for mats
    mat = [[None] * n for i in range(n)]

    # visited array to keep track
    # of visited nodes
    visited = [0] * n

    # Fill adjacency matrix
    buildGraph(arr, n, mat)

    # Since, we made a graph with contacts
    # as nodes with fields as links. Two
    # nodes are linked if they represent
    # the same person. So, total number of
    # connected components and nodes in each
    # component will be our answer.
    for i in range(n):
        if (not visited[i]):
            DFSvisit(i, mat, visited, sol, n)

            # Add delimeter to separate nodes
            # of one component from other.
            sol.append(-1)

    # Print the solution
    for i in range(len(sol)):
        if (sol[i] == -1):
            print()
        else:
            print(sol[i], end=" ")


# Driver Code
if __name__ == '__main__':
    arr = [contact("Gaurav", "gaurav@gmail.com", "gaurav@gfgQA.com"),
           contact("Lucky", "lucky@gmail.com", "+1234567"),
           contact("gaurav123", "+5412312", "gaurav123@skype.com"),
           contact("gaurav1993", "+5412312", "gaurav@gfgQA.com"),
           contact("raja", "+2231210", "raja@gfg.com"),
           contact("bahubali", "+878312", "raja")]

    n = len(arr)
    findSameContacts(arr, n)


