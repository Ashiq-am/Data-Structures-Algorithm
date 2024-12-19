# Python3 program to find maximum
# edges after adding which graph
# still remains a DAG
class Graph:

    def __init__(self, V):

        # No. of vertices
        self.V = V

        # Pointer to a list containing
        # adjacency list
        self.adj = [[] for i in range(V)]

        # Vector to store indegree of vertices
        self.indegree = [0 for i in range(V)]

    # Utility function to add edge
    def addEdge(self, v, w):

        # Add w to v's list.
        self.adj[v].append(w)

        # Increasing inner degree of w by 1
        self.indegree[w] += 1

    # Main function to print maximum
    # edges that can be added
    def topologicalSort(self):

        topological = []
        q = []

        # In starting append all node
        # with indegree 0
        for i in range(self.V):
            if (self.indegree[i] == 0):
                q.append(i)

        while (len(q) != 0):
            t = q[0]
            q.pop(0)

            # Append the node into topological
            # vector
            topological.append(t)

            # Reducing indegree of adjacent
            # vertices
            for j in self.adj[t]:
                self.indegree[j] -= 1

                # If indegree becomes 0, just
                # append into queue
                if (self.indegree[j] == 0):
                    q.append(j)

        return topological

    # The function prints all edges that
    # can be added without making any cycle
    # It uses recursive topologicalSort()
    def maximumEdgeAddtion(self):

        visited = [False for i in range(self.V)]

        topo = self.topologicalSort()

        # Looping for all nodes
        for i in range(len(topo)):
            t = topo[i]

            # In below loop we mark the
            # adjacent node of t
            for j in self.adj[t]:
                visited[j] = True

            # In below loop unmarked nodes
            # are printed
            for j in range(i + 1, len(topo)):

                # If not marked, then we can make
                # an edge between t and j
                if (not visited[topo[j]]):
                    print(str(t) + '-' +
                          str(topo[j]), end=' ')

                visited[topo[j]] = False


# Driver code
if __name__ == '__main__':
    # Create a graph given in the
    # above diagram
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)

    g.maximumEdgeAddtion()
