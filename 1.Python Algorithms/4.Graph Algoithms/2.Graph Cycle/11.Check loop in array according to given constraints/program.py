# Python3 program to check if a
# given array is cyclic or not

# A simple Graph DFS based recursive
# function to check if there is cycle
# in graph with vertex v as root of DFS.
# Refer below article for details.
# https:#www.geeksforgeeks.org/detect-cycle-in-a-graph/
def isCycleRec(v, adj, visited, recur):
    visited[v] = True
    recur[v] = True
    for i in range(len(adj[v])):
        if (visited[adj[v][i]] == False):
            if (isCycleRec(adj[v][i], adj,
                           visited, recur)):
                return True

        # There is a cycle if an adjacent is visited
        # and present in recursion call stack recur[]
        elif (visited[adj[v][i]] == True and
              recur[adj[v][i]] == True):
            return True

    recur[v] = False
    return False


# Returns true if arr[] has cycle
def isCycle(arr, n):
    # Create a graph using given
    # moves in arr[]
    adj = [[] for i in range(n)]
    for i in range(n):
        if (i != (i + arr[i] + n) % n):
            adj[i].append((i + arr[i] + n) % n)

    # Do DFS traversal of graph
    # to detect cycle
    visited = [False] * n
    recur = [False] * n
    for i in range(n):
        if (visited[i] == False):
            if (isCycleRec(i, adj,
                           visited, recur)):
                return True
    return True


# Driver code
if __name__ == '__main__':

    arr = [2, -1, 1, 2, 2]
    n = len(arr)
    if (isCycle(arr, n)):
        print("Yes")
    else:
        print("No")
