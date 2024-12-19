# Python3 program to calculate number
# of nodes between two nodes
import queue


# function to calculate no of nodes
# between two nodes
def totalNodes(adjac, n, x, y):
    # x is the source node and
    # y is destination node

    # visited array take account of
    # the nodes visited through the bfs
    visited = [0] * (n + 1)

    # parent array to store each nodes
    # parent value
    p = [None] * n

    q = queue.Queue()
    q.put(x)

    # take our first node(x) as first
    # element of queue and marked it as
    # visited through visited[] array
    visited[x] = True

    m = None

    # normal bfs method starts
    while (not q.empty()):
        m = q.get()
        for i in range(len(adjac[m])):
            h = adjac[m][i]
            if (not visited[h]):
                visited[h] = True

                # when new node is encountered
                # we assign it's parent value
                # in parent array p
                p[h] = m
                q.put(h)

    # count variable stores the result
    count = 0

    # loop start with parent of y
    # till we encountered x
    i = p[y]
    while (i != x):
        # count increases for counting
        # the nodes
        count += 1

        i = p[i]

    return count


# Driver Code
if __name__ == '__main__':
    # adjacency list for graph
    adjac = [[] for i in range(7)]

    # creating graph, keeping length of
    # adjacency list as (1 + no of nodes)
    # as index ranges from (0 to n-1)
    adjac[1].append(4)
    adjac[4].append(1)
    adjac[5].append(4)
    adjac[4].append(5)
    adjac[4].append(2)
    adjac[2].append(4)
    adjac[2].append(6)
    adjac[6].append(2)
    adjac[6].append(3)
    adjac[3].append(6)

    print(totalNodes(adjac, 7, 1, 3))
