# Python3 program to find out whether
# a given graph is Bipartite or not
import queue


# This function returns true if graph
# G[V][V] contains odd cycle, else false
def containsOdd(G, src):
    global V

    # Create a color array to store
    # colors assigned to all veritces.
    # Vertex number is used as index
    # in this array. The value '-1' of
    # colorArr[i] is used to indicate
    # that no color is assigned to vertex
    # 'i'. The value 1 is used to indicate
    # first color is assigned and value 0
    # indicates second color is assigned.
    colorArr = [-1] * V

    # Assign first color to source
    colorArr[src] = 1

    # Create a queue (FIFO) of vertex
    # numbers and enqueue source vertex
    # for BFS traversal
    q = queue.Queue()
    q.put(src)

    # Run while there are vertices in
    # queue (Similar to BFS)
    while (not q.empty()):

        # Dequeue a vertex from queue
        u = q.get()

        # Return true if there is a self-loop
        if (G[u][u] == 1):
            return True

        # Find all non-colored adjacent vertices
        for v in range(V):

            # An edge from u to v exists and
            # destination v is not colored
            if (G[u][v] and colorArr[v] == -1):

                # Assign alternate color to this
                # adjacent v of u
                colorArr[v] = 1 - colorArr[u]
                q.put(v)

            # An edge from u to v exists and
            # destination v is colored with
            # same color as u
            elif (G[u][v] and
                  colorArr[v] == colorArr[u]):
                return True

    # If we reach here, then all
    # adjacent vertices can be
    # colored with alternate color
    return False


# Driver Code
V = 4
G = [[0, 1, 0, 1],
     [1, 0, 1, 0],
     [0, 1, 0, 1],
     [1, 0, 1, 0]]

if containsOdd(G, 0):
    print("Yes")
else:
    print("No")
