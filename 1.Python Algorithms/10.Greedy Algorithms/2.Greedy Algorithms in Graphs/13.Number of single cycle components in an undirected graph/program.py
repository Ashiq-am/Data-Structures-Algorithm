# Python3 program to find single
# cycle components in a graph.
N = 100000

# degree of all the vertices
degree = [0] * N

# to keep track of all the
# vertices covered till now
found = [None] * N

# All the vertices in a particular
# connected component of the graph
curr_graph = []

# adjacency list
adj_list = [[] for i in range(N)]


# depth-first traversal to identify
# all the nodes in a particular
# connected graph component
def DFS(v):
    found[v] = True
    curr_graph.append(v)

    for it in adj_list[v]:
        if not found[it]:
            DFS(it)


# function to add an edge in the graph
def addEdge(adj_list, src, dest):
    # for index decrement both src and dest.
    src, dest = src - 1, dest - 1
    adj_list[src].append(dest)
    adj_list[dest].append(src)
    degree[src] += 1
    degree[dest] += 1


def countSingleCycles(n, m):
    # count of cycle graph components
    count = 0
    for i in range(0, n):
        if not found[i]:
            curr_graph.clear()
            DFS(i)

            # traversing the nodes of the
            # current graph component
            flag = 1
            for v in curr_graph:
                if degree[v] == 2:
                    continue
                else:
                    flag = 0
                    break

            if flag == 1:
                count += 1

    return count


# Driver Code
if __name__ == "__main__":
    # n->number of vertices
    # m->number of edges
    n, m = 15, 14
    addEdge(adj_list, 1, 10)
    addEdge(adj_list, 1, 5)
    addEdge(adj_list, 5, 10)
    addEdge(adj_list, 2, 9)
    addEdge(adj_list, 9, 15)
    addEdge(adj_list, 2, 15)
    addEdge(adj_list, 2, 12)
    addEdge(adj_list, 12, 15)
    addEdge(adj_list, 13, 8)
    addEdge(adj_list, 6, 14)
    addEdge(adj_list, 14, 3)
    addEdge(adj_list, 3, 7)
    addEdge(adj_list, 7, 11)
    addEdge(adj_list, 11, 6)

    print(countSingleCycles(n, m))
