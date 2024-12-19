# Python3 code to perform DFS of given tree :

# DFS on tree
def dfs(List, node, arrival):
    # Printing traversed node
    print(node)

    # Traversing adjacent edges
    for i in range(len(List[node])):

        # Not traversing the parent node
        if (List[node][i] != arrival):
            dfs(List, List[node][i], node)


# Driver Code
if __name__ == '__main__':
    # Number of nodes
    nodes = 5

    # Adjacency List
    List = [[] for i in range(10000)]

    # Designing the tree
    List[1].append(2)
    List[2].append(1)

    List[1].append(3)
    List[3].append(1)

    List[2].append(4)
    List[4].append(2)

    List[3].append(5)
    List[5].append(3)

    # Function call
    dfs(List, 1, 0)
