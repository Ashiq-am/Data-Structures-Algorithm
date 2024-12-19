# Python3 code to find the sub-tree
# with minimum color difference
# in a 2-coloured tree

# Tree traversal to compute minimum difference
def dfs(node, parent, tree, colour, answer):
    # Initial min difference is
    # the color of node
    answer[node] = colour[node]

    # Traversing its children
    for u in tree[node]:

        # Not traversing the parent
        if (u == parent):
            continue

        dfs(u, node, tree, colour, answer)

        # If the child is Adding positively to
        # difference, we include it in the answer
        # Otherwise, we leave the sub-tree and
        # include 0 (nothing) in the answer
        answer[node] += max(answer[u], 0)


def maxDiff(tree, colour, N):
    answer = [0 for _ in range(N + 1)]

    # DFS for colour difference : 1colour - 2colour
    dfs(1, 0, tree, colour, answer)

    # Minimum colour difference is
    # maximum answer value
    high = 0
    for i in range(1, N + 1):
        high = max(high, answer[i])

        # Clearing the current value
        # to check for colour2 as well
        answer[i] = 0

    # Interchanging the colours
    for i in range(1, N + 1):
        if colour[i] == -1:
            colour[i] = 1
        else:
            colour[i] = -1

    # DFS for colour difference : 2colour - 1colour
    dfs(1, 0, tree, colour, answer)

    # Checking if colour2 makes the
    # minimum colour difference
    for i in range(1, N):
        high = max(high, answer[i])

    return high


# Driver code
# Nodes
N = 5

# Adjacency list representation
tree = [list() for _ in range(N + 1)]

# Edges
tree[1].append(2)
tree[2].append(1)
tree[1].append(3)
tree[3].append(1)
tree[2].append(4)
tree[4].append(2)
tree[3].append(5)
tree[5].append(3)

# Index represent the colour of that node
# There is no Node 0, so we start from
# index 1 to N
colour = [0, 1, 1, -1, -1, 1]

# Printing the result
print(maxDiff(tree, colour, N))
