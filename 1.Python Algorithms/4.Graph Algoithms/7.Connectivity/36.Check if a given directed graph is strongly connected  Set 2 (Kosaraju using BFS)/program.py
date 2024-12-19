# Python3 program to check if a given directed graph
# is strongly connected or not with BFS use
from collections import deque


# A recursive function to prDFS starting from v
def BFSUtil(adj, v, visited):
    # Create a queue for BFS
    queue = deque()

    # Mark the current node as visited
    # and enqueue it
    visited[v] = True
    queue.append(v)

    # 'i' will be used to get all adjacent
    # vertices of a vertex
    while (len(queue) > 0):

        # Dequeue a vertex from queue
        v = queue.popleft()
        # print(v)
        # queue.pop_front()

        # Get all adjacent vertices of the
        # dequeued vertex s. If a adjacent
        # has not been visited, then mark it
        # visited and enqueue it
        for i in adj[v]:
            if (visited[i] == False):
                visited[i] = True
                queue.append(i)

    return visited


# Function that returns reverse
# (or transpose) of this graph
def getTranspose(adj, V):
    g = [[] for i in range(V)]

    for v in range(V):

        # Recur for all the vertices adjacent to
        # this vertex
        # list<int>::iterator i
        for i in adj[v]:
            g[i].append(v)

    return g


def addEdge(adj, v, w):
    # Add w to v’s list.
    adj[v].append(w)
    return adj


# The main function that returns True if graph
# is strongly connected
def isSC(adj, V):
    # St1p 1: Mark all the vertices as not
    # visited (For first BFS)
    visited = [False] * V

    # Step 2: Do BFS traversal starting
    # from first vertex.
    visited = BFSUtil(adj, 0, visited)
    # print(visited)

    # If BFS traversal doesn’t visit all
    # vertices, then return false.
    for i in range(V):
        if (visited[i] == False):
            return False

    # Step 3: Create a reversed graph
    adj = getTranspose(adj, V)

    # Step 4: Mark all the vertices as not
    # visited (For second BFS)
    for i in range(V):
        visited[i] = False

    # Step 5: Do BFS for reversed graph
    # starting from first vertex.
    # Staring Vertex must be same starting
    # poof first DFS
    visited = BFSUtil(adj, 0, visited)

    # If all vertices are not visited in
    # second DFS, then return false
    for i in range(V):
        if (visited[i] == False):
            return False

    return True


# Driver code
if __name__ == '__main__':
    # Create graphs given in the above diagrams
    g1 = [[] for i in range(5)]
    g1 = addEdge(g1, 0, 1)
    g1 = addEdge(g1, 1, 2)
    g1 = addEdge(g1, 2, 3)
    g1 = addEdge(g1, 3, 0)
    g1 = addEdge(g1, 2, 4)
    g1 = addEdge(g1, 4, 2)
    # print(g1)

    print("Yes" if isSC(g1, 5) else "No")

    g2 = [[] for i in range(4)]

    g2 = addEdge(g2, 0, 1)
    g2 = addEdge(g2, 1, 2)
    g2 = addEdge(g2, 2, 3)

    print("Yes" if isSC(g2, 4) else "No")
