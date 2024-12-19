# Python3 program to find the sum
# of dependencies

# To add an edge
def addEdge(adj, u, v):
    adj[u].append(v)


# Find the sum of all dependencies
def findSum(adj, V):
    sum = 0

    # Just find the size at each
    # vector's index
    for u in range(V):
        sum += len(adj[u])

    return sum


# Driver code
if __name__ == '__main__':
    V = 4
    adj = [[] for i in range(V)]

    addEdge(adj, 0, 2)
    addEdge(adj, 0, 3)
    addEdge(adj, 1, 3)
    addEdge(adj, 2, 3)

    print("Sum of dependencies is",findSum(adj, V))
