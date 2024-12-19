# python Program to find number of
# cycles of length k in a graph
# with n nodes.

# Return the Number of ways from a
# node to make a loop of size K in
# undirected complete connected
# graph of N nodes
def numOfways(n, k):
    p = 1

    if (k % 2):
        p = -1

    return (pow(n - 1, k) + p * (n - 1)) / n


# Driver code
n = 4
k = 2
print(numOfways(n, k))
