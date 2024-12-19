# Python3 program to check if removing
# an edge disconnects a graph or not.

# Graph class represents a directed graph
# using adjacency list representation
class Graph:

    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def addEdge(self, u, v):
        self.adj[u].append(v)  # Add w to v’s list.
        self.adj[v].append(u)  # Add w to v’s list.

    def DFS(self, v, visited):

        # Mark the current node as
        # visited and print it
        visited[v] = True

        # Recur for all the vertices
        # adjacent to this vertex
        i = 0
        while i != len(self.adj[v]):
            if (not visited[self.adj[v][i]]):
                self.DFS(self.adj[v][i], visited)
            i += 1

    # Returns true if given graph is
    # connected, else false
    def isConnected(self):
        visited = [False] * self.V

        # Find all reachable vertices
        # from first vertex
        self.DFS(0, visited)

        # If set of reachable vertices
        # includes all, return true.
        for i in range(1, self.V):
            if (visited[i] == False):
                return False

        return True

    # This function assumes that edge
    # (u, v) exists in graph or not,
    def isBridge(self, u, v):

        # Remove edge from undirected graph
        indU = self.adj[v].index(u)
        indV = self.adj[u].index(v)
        del self.adj[u][indV]
        del self.adj[v][indU]

        res = self.isConnected()

        # Adding the edge back
        self.addEdge(u, v)

        # Return true if graph becomes
        # disconnected after removing
        # the edge.
        return (res == False)


# Driver code
if __name__ == '__main__':

    # Create a graph given in the
    # above diagram
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 3)

    if g.isBridge(1, 2):
        print("Yes")
    else:
        print("No")
