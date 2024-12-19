# Python3 program to count number of pair of
# positions in matrix which are not accessible

# Counts number of vertices connected in a
# component containing x. Stores the count in k.
def dfs(graph, visited, x, k):
    for i in range(len(graph[x])):
        if (not visited[graph[x][i]]):
            # Incrementing the number of node
            # in a connected component.
            k[0] += 1

            visited[graph[x][i]] = True
            dfs(graph, visited, graph[x][i], k)


# Return the number of count of
# non-accessible cells.
def countNonAccessible(graph, N):
    visited = [False] * (N * N + N)

    ans = 0
    for i in range(1, N * N + 1):
        if (not visited[i]):
            visited[i] = True

            # Initialize count of connected
            # vertices found by DFS starting
            # from i.
            k = [1]
            dfs(graph, visited, i, k)

            # Update result
            ans += k[0] * (N * N - k[0])
    return ans


# Inserting the edge between edge.
def insertpath(graph, N, x1, y1, x2, y2):
    # Mapping the cell coordinate
    # into node number.
    a = (x1 - 1) * N + y1
    b = (x2 - 1) * N + y2

    # Inserting the edge.
    graph[a].append(b)
    graph[b].append(a)


# Driver Code
if __name__ == '__main__':
    N = 2

    graph = [[] for i in range(N * N + 1)]

    insertpath(graph, N, 1, 1, 1, 2)
    insertpath(graph, N, 1, 2, 2, 2)

    print(countNonAccessible(graph, N))
