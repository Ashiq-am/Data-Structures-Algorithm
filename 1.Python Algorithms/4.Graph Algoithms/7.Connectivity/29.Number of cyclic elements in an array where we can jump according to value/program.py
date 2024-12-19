# Python3 program to count cyclic points
# in an array using Kosaraju's Algorithm

# Counts number of nodes reachable
# from v
def DFSUtil(v):
    global visited, adj

    visited[v] = True
    ans = 1

    for i in adj[v]:
        if (not visited[i]):
            ans += DFSUtil(i)

    return ans


def getTranspose():
    global visited, adj

    for v in range(5):
        for i in adj[v]:
            adj[i].append(v)


def addEdge(v, w):
    global visited, adj
    adj[v].append(w)


def fillOrder(v):
    global Stack, adj, visited
    visited[v] = True

    for i in adj[v]:
        if (not visited[i]):
            fillOrder(i)

    Stack.append(v)


# This function mainly returns total count of
# nodes in individual SCCs using Kosaraju's
# algorithm.
def countSCCNodes():
    global adj, visited, S
    res = 0

    # stack<int> Stack;
    # bool* visited = new bool[V];
    for i in range(5):
        if (visited[i] == False):
            fillOrder(i)

    getTranspose()
    for i in range(5):
        visited[i] = False

    while (len(Stack) > 0):
        v = Stack[-1]
        del Stack[-1]

        if (visited[v] == False):
            ans = DFSUtil(v)
            if (ans > 1):
                res += ans

    return res


# Returns count of cyclic elements in arr[]
def countCyclic(arr, n):
    global adj
    res = 0

    # Create a graph of array elements
    for i in range(1, n + 1):
        x = arr[i - 1]

        # If i + arr[i-1] jumps beyond last
        # element, we take mod considering
        # cyclic array
        v = (x + i) % n + 1

        # If there is a self loop, we
        # increment count of cyclic points.
        if (i == v):
            res += 1

        addEdge(i, v)

    # Add nodes of strongly connected components
    # of size more than 1.
    res += countSCCNodes()

    return res


# Driver code
if __name__ == '__main__':
    adj = [[] for i in range(100)]
    visited = [False for i in range(100)]
    arr = [1, 1, 1, 1]
    Stack = []
    n = len(arr)

    print(countCyclic(arr, n))


