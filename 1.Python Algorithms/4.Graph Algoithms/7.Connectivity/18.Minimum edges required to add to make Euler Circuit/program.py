# Python3 program to find minimum edge
# required to make Euler Circuit

# Depth-First Search to find a
# connected component
def dfs(g, vis, odd, deg, comp, v):
    vis[v] = 1

    if (deg[v] % 2 == 1):
        odd[comp] += 1

    for u in range(len(g[v])):
        if (vis[u] == 0):
            dfs(g, vis, odd, deg, comp, u)


# Return minimum edge required to
# make Euler Circuit
def minEdge(n, m, s, d):
    # g : to store adjacency list
    #	 representation of graph.
    # e : to store list of even degree vertices
    # o : to store list of odd degree vertices
    g = [[] for i in range(n + 1)]
    e = []
    o = []

    deg = [0] * (n + 1)  # Degrees of vertices
    vis = [0] * (n + 1)  # To store visited in DFS
    odd = [0] * (n + 1)  # Number of odd nodes
    # in components

    for i in range(m):
        g[s[i]].append(d[i])
        g[d[i]].append(s[i])
        deg[s[i]] += 1
        deg[d[i]] += 1

    # 'ans' is result and 'comp'
    # is component id
    ans = 0
    comp = 0
    for i in range(1, n + 1):
        if (vis[i] == 0):
            comp += 1
            dfs(g, vis, odd, deg, comp, i)

            # Checking if connected component
            # is odd.
            if (odd[comp] == 0):
                e.append(comp)

            # Checking if connected component
            # is even.
            else:
                o.append(comp)

    # If whole graph is a single connected
    # component with even degree.
    if (len(o) == 0 and len(e) == 1):
        return 0

    # If all connected component is even
    if (len(o) == 0):
        return len(e)

    # If graph have atleast one
    # even connected component
    if (len(e) != 0):
        ans += len(e)

    # For all the odd connected component.
    for i in range(len(o)):
        ans += odd[i] // 2

    return ans


# Driver Code
if __name__ == '__main__':
    n = 3
    m = 2
    source = [1, 2]
    destination = [2, 3]

    print(minEdge(n, m, source, destination))


