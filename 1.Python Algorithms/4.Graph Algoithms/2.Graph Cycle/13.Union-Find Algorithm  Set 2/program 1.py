# Naive implementation of find
def find(parent, i):
    if (parent[i] == -1):
        return i

    return find(parent, parent[i])


# Naive implementation of union()
def Union(parent, x, y):
    xset = find(parent, x)
    yset = find(parent, y)
    parent[xset] = yset
