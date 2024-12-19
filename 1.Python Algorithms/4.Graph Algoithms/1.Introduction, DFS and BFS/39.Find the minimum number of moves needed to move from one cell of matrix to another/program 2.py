# Python3 program for the above approach

# To be used in DFS while comparing the
# minimum element
# define MAX (I4T_MAX - 1)
visited = {}
adj = [[] for i in range(16)]


# Performing the DFS for the minimum moves
def add_edges(u, v):
    global adj
    adj[u].append(v)


def DFS(s, d):
    global visited

    # Base condition for the recursion
    if (s == d):
        return 0

    # Initializing the result
    res = 10 ** 9
    visited[s] = 1

    for item in adj[s]:
        if (item not in visited):
            # Comparing the res with
            # the result of DFS
            # to get the minimum moves
            res = min(res, 1 + DFS(item, d))

    return res


# Ruling out the cases where the element
# to be inserted is outside the matrix
def is_safe(arr, i, j):
    if ((i < 0 or i >= 4) or
            (j < 0 or j >= 4) or arr[i][j] == 0):
        return False

    return True


def min_moves(arr):
    s, d, V = -1, -1, 16
    # k be the variable which represents the
    # positions( 0 - 4*4 ) inside the graph.

    # k moves from top-left to bottom-right
    k = 0
    for i in range(4):
        for j in range(4):

            # Adding the edge
            if (arr[i][j] != 0):
                if (is_safe(arr, i, j + 1)):
                    add_edges(k, k + 1)  # left
                if (is_safe(arr, i, j - 1)):
                    add_edges(k, k - 1)  # right
                if (is_safe(arr, i + 1, j)):
                    add_edges(k, k + 4)  # bottom
                if (is_safe(arr, i - 1, j)):
                    add_edges(k, k - 4)  # top

            # Source from which DFS to be
            # performed
            if (arr[i][j] == 1):
                s = k

            # Destination
            elif (arr[i][j] == 2):
                d = k

            # Moving k from top-left
            # to bottom-right
            k += 1

    # DFS performed from
    # source to destination
    return DFS(s, d)


# Driver code
if __name__ == '__main__':
    arr = [[3, 3, 1, 0],
           [3, 0, 3, 3],
           [2, 3, 0, 3],
           [0, 3, 3, 3]]

    # If(min_moves(arr) == MAX) there
    # doesn't exist a path
    # from source to destination
    print(min_moves(arr))
