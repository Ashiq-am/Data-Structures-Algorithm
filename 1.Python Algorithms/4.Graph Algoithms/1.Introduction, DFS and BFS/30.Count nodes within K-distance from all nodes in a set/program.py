# Python3 program to count nodes inside
# K distance range from marked nodes
import queue


# Utility bfs method to fill distance
# vector and returns most distant
# marked node from node u
def bfsWithDistance(g, mark, u, dis):
    lastMarked = 0
    q = queue.Queue()

    # push node u in queue and initialize
    # its distance as 0
    q.put(u)
    dis[u] = 0

    # loop untill all nodes are processed
    while (not q.empty()):
        u = q.get()

        # if node is marked, update
        # lastMarked variable
        if (mark[u]):
            lastMarked = u

        # loop over all neighbors of u and
        # update their distance before
        # pushing in queue
        for i in range(len(g[u])):
            v = g[u][i]

            # if not given value already
            if (dis[v] == -1):
                dis[v] = dis[u] + 1
                q.put(v)

    # return last updated marked value
    return lastMarked


# method returns count of nodes which
# are in K-distance range from marked nodes
def nodesKDistanceFromMarked(edges, V, marked, N, K):
    # vertices in a tree are one
    # more than number of edges
    V = V + 1
    g = [[] for i in range(V)]

    # fill vector for graph
    u, v = 0, 0
    for i in range(V - 1):
        u = edges[i][0]
        v = edges[i][1]

        g[u].append(v)
        g[v].append(u)

    # fill boolean array mark from
    # marked array
    mark = [False] * V
    for i in range(N):
        mark[marked[i]] = True

    # vectors to store distances
    tmp = [-1] * V
    dl = [-1] * V
    dr = [-1] * V

    # first bfs(from any random node)
    # to get one distant marked node
    u = bfsWithDistance(g, mark, 0, tmp)

    # second bfs to get other distant
    # marked node and also dl is filled
    # with distances from first chosen
    # marked node
    u = bfsWithDistance(g, mark, u, dl)

    # third bfs to fill dr by distances
    # from second chosen marked node
    bfsWithDistance(g, mark, u, dr)

    res = 0

    # loop over all nodes
    for i in range(V):

        # increase res by 1, if current node
        # has distance less than K from both
        # extreme nodes
        if (dl[i] <= K and dr[i] <= K):
            res += 1
    return res


# Driver Code
if __name__ == '__main__':
    edges = [[1, 0], [0, 3], [0, 8],
             [2, 3], [3, 5], [3, 6],
             [3, 7], [4, 5], [5, 9]]
    V = len(edges)

    marked = [1, 2, 4]
    N = len(marked)

    K = 3
    print(nodesKDistanceFromMarked(edges, V,marked, N, K))


