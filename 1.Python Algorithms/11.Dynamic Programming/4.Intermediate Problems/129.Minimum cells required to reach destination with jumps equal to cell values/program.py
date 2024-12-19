# Python3 implementation to count minimum cells required
# to be covered to reach destination
SIZE = 100
MAX = 10000000


# function to count minimum cells required
# to be covered to reach destination
def minCells(mat, m, n):
    # to store min cells required to be
    # covered to reach a particular cell
    dp = [[MAX for i in range(n)] for i in range(m)]

    # initially no cells can be reached

    # base case
    dp[0][0] = 1

    # building up the dp[][] matrix
    for i in range(m):
        for j in range(n):
            # dp[i][j] != MAX denotes that cell (i, j)
            # can be reached from cell (0, 0) and the other
            # half of the condition finds the cell on the
            # right that can be reached from (i, j)
            if (dp[i][j] != MAX and
                    (j + mat[i][j]) < n and
                    (dp[i][j] + 1) < dp[i][j + mat[i][j]]):
                dp[i][j + mat[i][j]] = dp[i][j] + 1

            # the other half of the condition finds the cell
            # right below that can be reached from (i, j)
            if (dp[i][j] != MAX and (i + mat[i][j]) < m
                    and (dp[i][j] + 1) < dp[i + mat[i][j]][j]):
                dp[i + mat[i][j]][j] = dp[i][j] + 1

    # it true then cell (m-1, n-1) can be reached
    # from cell (0, 0) and returns the minimum
    # number of cells covered
    if (dp[m - 1][n - 1] != MAX):
        return dp[m - 1][n - 1]

    # cell (m-1, n-1) cannot be reached from
    # cell (0, 0)
    return -1


# Driver program to test above
mat = [[2, 3, 2, 1, 4],
       [3, 2, 5, 8, 2],
       [1, 1, 2, 2, 1]]

m = 3
n = 5
print("Minimum number of cells = ",minCells(mat, m, n))
