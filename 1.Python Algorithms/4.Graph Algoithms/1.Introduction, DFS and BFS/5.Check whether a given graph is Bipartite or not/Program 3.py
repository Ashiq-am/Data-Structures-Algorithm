# Python3 program to find out whether a given
# graph is Bipartite or not using recursion.
V = 4


def colorGraph(G, color, pos, c):
    if color[pos] != -1 and color[pos] != c:
        return False

    # color this pos as c and all its neighbours and 1-c
    color[pos] = c
    ans = True
    for i in range(0, V):
        if G[pos][i]:
            if color[i] == -1:
                ans &= colorGraph(G, color, i, 1 - c)

            if color[i] != -1 and color[i] != 1 - c:
                return False

        if not ans:
            return False

    return True


def isBipartite(G):
    color = [-1] * V

    # start is vertex 0
    pos = 0
    # two colors 1 and 0
    return colorGraph(G, color, pos, 1)


if __name__ == "__main__":

    G = [[0, 1, 0, 1],
         [1, 0, 1, 0],
         [0, 1, 0, 1],
         [1, 0, 1, 0]]

    if isBipartite(G):
        print("Yes")
    else:
        print("No")
