# Python3 program to find shortest weighted
# cycle in undirected graph
from sys import maxsize

INF = int(0x3f3f3f3f)


class Edge:

    def __init__(self, u: int,
                 v: int,
                 weight: int) -> None:
        self.u = u
        self.v = v
        self.weight = weight


# Weighted undirected Graph
class Graph:

    def __init__(self, V: int) -> None:

        self.V = V
        self.adj = [[] for _ in range(V)]

        # Used to store all edge information
        self.edge = []

    # Function add edge to graph
    def addEdge(self, u: int,
                v: int,
                w: int) -> None:

        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

        # Add Edge to edge list
        e = Edge(u, v, w)
        self.edge.append(e)

    # Function remove edge from undirected graph
    def removeEdge(self, u: int,
                   v: int, w: int) -> None:

        self.adj[u].remove((v, w))
        self.adj[v].remove((u, w))

    # Find the shortest path from source
    # to sink using Dijkstra’s shortest
    # path algorithm [ Time complexity
    # O(E logV )]
    def ShortestPath(self, u: int, v: int) -> int:

        # Create a set to store vertices that
        # are being preprocessed
        setds = set()

        # Create a vector for distances and
        # initialize all distances as infinite (INF)
        dist = [INF] * self.V

        # Insert source itself in Set and
        # initialize its distance as 0.
        setds.add((0, u))
        dist[u] = 0

        # Looping till all shortest distance are
        # finalized then setds will become empty
        while (setds):

            # The first vertex in Set is the minimum
            # distance vertex, extract it from set.
            tmp = setds.pop()

            # Vertex label is stored in second of
            # pair (it has to be done this way to
            # keep the vertices sorted distance
            # (distance must be first item in pair)
            uu = tmp[1]

            # 'i' is used to get all adjacent
            # vertices of a vertex
            for i in self.adj[uu]:

                # Get vertex label and weight of
                # current adjacent of u.
                vv = i[0]
                weight = i[1]

                # If there is shorter path to v through u.
                if (dist[vv] > dist[uu] + weight):

                    # If the distance of v is not INF then
                    # it must be in our set, so removing it
                    # and inserting again with updated less
                    # distance. Note : We extract only those
                    # vertices from Set for which distance
                    # is finalized. So for them, we would
                    # never reach here.
                    if (dist[vv] != INF):
                        if ((dist[vv], vv) in setds):
                            setds.remove((dist[vv], vv))

                    # Updating distance of v
                    dist[vv] = dist[uu] + weight
                    setds.add((dist[vv], vv))

        # Return shortest path from
        # current source to sink
        return dist[v]

    # Function return minimum weighted cycle
    def FindMinimumCycle(self) -> int:

        min_cycle = maxsize
        E = len(self.edge)

        for i in range(E):
            # Current Edge information
            e = self.edge[i]

            # Get current edge vertices which we currently
            # remove from graph and then find shortest path
            # between these two vertex using Dijkstra’s
            # shortest path algorithm .
            self.removeEdge(e.u, e.v, e.weight)

            # Minimum distance between these two vertices
            distance = self.ShortestPath(e.u, e.v)

            # To make a cycle we have to add weight of
            # currently removed edge if this is the
            # shortest cycle then update min_cycle
            min_cycle = min(min_cycle,
                            distance + e.weight)

            # Add current edge back to the graph
            self.addEdge(e.u, e.v, e.weight)

        # Return shortest cycle
        return min_cycle


# Driver Code
if __name__ == "__main__":
    V = 9

    g = Graph(V)

    # Making above shown graph
    g.addEdge(0, 1, 4)
    g.addEdge(0, 7, 8)
    g.addEdge(1, 2, 8)
    g.addEdge(1, 7, 11)
    g.addEdge(2, 3, 7)
    g.addEdge(2, 8, 2)
    g.addEdge(2, 5, 4)
    g.addEdge(3, 4, 9)
    g.addEdge(3, 5, 14)
    g.addEdge(4, 5, 10)
    g.addEdge(5, 6, 2)
    g.addEdge(6, 7, 1)
    g.addEdge(6, 8, 6)
    g.addEdge(7, 8, 7)

    print(g.FindMinimumCycle())
