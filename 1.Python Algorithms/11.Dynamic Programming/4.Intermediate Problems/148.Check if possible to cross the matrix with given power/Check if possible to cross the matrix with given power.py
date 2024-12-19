# Python3 program to find if it is possible to cross
# the matrix with given power
N = 105
R = 3
C = 4


def maximumValue(n, m, p, grid):
    dp = [[[False for i in range(N)] for j in range(N)] for k in range(N)]

    # For each value of dp[i][j][k]
    for i in range(n):
        for j in range(m):
            k = grid[i][j]
            while (k <= p):

                # For first cell and for each value of k
                if (i == 0 and j == 0):
                    if (k == grid[i][j]):
                        dp[i][j][k] = True

                # For first cell of each row
                elif (i == 0):
                    dp[i][j][k] = (dp[i][j][k] or
                                   dp[i][j - 1][k - grid[i][j]])

                # For first cell of each column
                elif (j == 0):
                    dp[i][j][k] = (dp[i][j][k] or
                                   dp[i - 1][j][k - grid[i][j]])

                # For rest of the cell
                else:

                    # Down movement.
                    dp[i][j][k] = (dp[i][j][k] or
                                   dp[i][j - 1][k - grid[i][j]])

                    # Right movement.
                    dp[i][j][k] = (dp[i][j][k] or
                                   dp[i - 1][j][k - grid[i][j]])

                    # Diagonal movement.
                    dp[i][j][k] = (dp[i][j][k] or
                                   dp[i - 1][j - 1][k - grid[i][j]])
                k += 1

    # Finding maximum k.
    ans = k
    while (ans >= 0):
        if (dp[n - 1][m - 1][ans]):
            break
        ans -= 1

    return ans


# Driver Code
n = 3
m = 4
p = 9
grid = [[2, 3, 4, 1], [6, 5, 5, 3], [5, 2, 3, 4]]

print(maximumValue(n, m, p, grid))
