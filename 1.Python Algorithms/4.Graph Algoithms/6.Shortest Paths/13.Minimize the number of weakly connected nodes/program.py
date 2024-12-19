# Python3 code to minimize the number
# of weakly connected nodes

# Set of nodes which are traversed
# in each launch of the DFS
node = set()
Graph = [[] for i in range(10001)]


# Function traversing the graph using DFS
# approach and updating the set of nodes
def dfs(visit, src):
    visit[src] = True
    node.add(src)
    llen = len(Graph[src])

    for i in range(llen):
        if (not visit[Graph[src][i]]):
            dfs(visit, Graph[src][i])


# Building a undirected graph
def buildGraph(x, y, llen):
    for i in range(llen):
        p = x[i]
        q = y[i]
        Graph[p].append(q)
        Graph[q].append(p)


# Computes the minimum number of disconnected
# components when a bi-directed graph is
# converted to a undirected graph
def compute(n):
    # Declaring and initializing
    # a visited array
    visit = [False for i in range(n + 5)]

    number_of_nodes = 0

    # We check if each node is
    # visited once or not
    for i in range(n):

        # We only launch DFS from a
        # node iff it is unvisited.
        if (not visit[i]):

            # Clearing the set of nodes
            # on every relaunch of DFS
            node.clear()

            # Relaunching DFS from an
            # unvisited node.
            dfs(visit, i)

            # Iterating over the node set to count the
            # number of nodes visited after making the
            # graph directed and storing it in the
            # variable count. If count / 2 == number
            # of nodes - 1, then increment count by 1.
            count = 0

            for it in node:
                count += len(Graph[(it)])

            count //= 2

            if (count == len(node) - 1):
                number_of_nodes += 1

    return number_of_nodes


# Driver code
if __name__ == '__main__':
    n = 6
    m = 4
    x = [1, 1, 4, 4, 0, 0, 0, 0, 0]
    y = [2, 3, 5, 6, 0, 0, 0, 0, 0]

    '''For given x and y above, graph is as below :
        1-----2		 4------5
        |			 |
        |			 |
        |			 |
        3			 6

        # Note : This code will work for
        # connected graph also as :
        1-----2
        |	 | \
        |	 | \
        |	 | \
        3-----4----5
    '''

    # Building graph in the form of a adjacency list
    buildGraph(x, y, n)

    print(str(compute(n)) + " weakly connected nodes")


