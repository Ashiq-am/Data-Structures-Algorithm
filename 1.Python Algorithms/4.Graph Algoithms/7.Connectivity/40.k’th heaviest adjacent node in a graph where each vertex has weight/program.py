# Python3 program to find Kth node
# weight after sorting of nodes
# directly connected to a node.

# PrKth node number for each node
# after sorting connected node
# according to their weight.
def printkthnode(adj, wt, n, k):
    # Sort Adjacency List of all
    # node on the basis of its weight.
    for i in range(n):
        adj[i].sort()

    # Printing Kth node for each node.
    for i in range(n):
        if (len(adj[i]) >= k):
            print(adj[i][len(adj[i]) -
                         k][1], end=" ")
        else:
            print("-1", end=" ")


# Driver Code
if __name__ == '__main__':
    n = 3
    k = 2
    wt = [2, 4, 3]

    # Making adjacency list, storing
    # the nodes along with their weight.
    adj = [[] for i in range(n + 1)]

    adj[0].append([wt[2], 2])
    adj[2].append([wt[0], 0])

    adj[0].append([wt[1], 1])
    adj[1].append([wt[0], 0])

    adj[1].append([wt[2], 2])
    adj[2].append([wt[1], 1])

    printkthnode(adj, wt, n, k)
