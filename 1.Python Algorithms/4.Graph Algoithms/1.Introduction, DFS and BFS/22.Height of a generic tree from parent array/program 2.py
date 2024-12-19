# Python3 code to find height of N-ary
# tree in O(n) (Efficient Approach)

# Recur For Ancestors of node and
# store height of node at last
def fillHeight(p, node, visited, height):
    # If root node
    if (p[node] == -1):
        # mark root node as visited
        visited[node] = 1
        return 0

    # If node is already visited
    if (visited[node]):
        return height[node]

    # Visit node and calculate its height
    visited[node] = 1

    # recur for the parent node
    height[node] = 1 + fillHeight(p, p[node],
                                  visited, height)

    # return calculated height for node
    return height[node]


def findHeight(parent, n):
    # To store max height
    ma = 0

    # To check whether or not node is
    # visited before
    visited = [0] * n

    # For Storing Height of node
    height = [0] * n

    for i in range(n):

        # If not visited before
        if (not visited[i]):
            height[i] = fillHeight(parent, i,
                                   visited, height)

        # store maximum height so far
        ma = max(ma, height[i])

    return ma


# Driver Code
if __name__ == '__main__':
    parent = [-1, 0, 0, 0, 3, 1, 1, 2]
    n = len(parent)

    print("Height of N-ary Tree =",findHeight(parent, n))
