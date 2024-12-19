# Python code to count the singleton sub-graphs
# in a disconnected graph

# Function to compute the count
def compute(graph, N):
    # Storing intermediate result
    count = 0

    # Traversing the Nodes
    for i in range(1, N + 1):

        # Singleton component
        if (len(graph[i]) == 0):
            count += 1

    # Returning the result
    return count


# Driver
if __name__ == '__main__':
    # Number of nodes
    N = 6

    # Adjacency list for edges 1..6
    graph = [[] for i in range(7)]

    # Representing edges
    graph[1].append(2)
    graph[2].append(1)

    graph[2].append(3)
    graph[3].append(2)

    graph[5].append(6)
    graph[6].append(5)

    print(compute(graph, N))
