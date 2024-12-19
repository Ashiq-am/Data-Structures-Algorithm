# Python3 program to count numbers of k
# digits that are strictly monotone.

DP_s = 9


def getNumStrictMonotone(ln):
    # DP[i][j] is going to store monotone
    # numbers of length i+1 considering
    # j+1 digits (1, 2, 3, ..9)
    DP = [[0] * DP_s for _ in range(ln)]

    # Unit length numbers
    for i in range(DP_s):
        DP[0][i] = i + 1

    # Building dp[] in bottom up
    for i in range(1, ln):

        for j in range(1, DP_s):
            DP[i][j] = DP[i - 1][j - 1] + DP[i][j - 1]

    return DP[ln - 1][DP_s - 1]


# Driver code
print(getNumStrictMonotone(2))
