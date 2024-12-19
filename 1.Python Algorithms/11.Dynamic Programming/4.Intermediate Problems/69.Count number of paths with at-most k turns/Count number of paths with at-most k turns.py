# Python3 program to count number of paths
# with maximum k turns allowed
MAX = 100

# table to store results of subproblems
dp = [[[[-1 for col in range(2)]
        for col in range(MAX)]
       for row in range(MAX)]
      for row in range(MAX)]


# Returns count of paths to reach
# (i, j) from (0, 0) using at-most k turns.
# d is current direction, d = 0 indicates
# along row, d = 1 indicates along column.
def countPathsUtil(i, j, k, d):
    # If invalid row or column indexes
    if (i < 0 or j < 0):
        return 0

    # If current cell is top left itself
    if (i == 0 and j == 0):
        return 1

    # If 0 turns left
    if (k == 0):

        # If direction is row, then we can reach here
        # only if direction is row and row is 0.
        if (d == 0 and i == 0):
            return 1

        # If direction is column, then we can reach here
        # only if direction is column and column is 0.
        if (d == 1 and j == 0):
            return 1

        return 0

    # If this subproblem is already evaluated
    if (dp[i][j][k][d] != -1):
        return dp[i][j][k][d]

    # If current direction is row,
    # then count paths for two cases
    # 1) We reach here through previous row.
    # 2) We reach here through previous column,
    # so number of turns k reduce by 1.
    if (d == 0):
        dp[i][j][k][d] = countPathsUtil(i, j - 1, k, d) + \
                         countPathsUtil(i - 1, j, k - 1, not d)
        return dp[i][j][k][d]

    # Similar to above if direction is column
    dp[i][j][k][d] = countPathsUtil(i - 1, j, k, d) + \
                     countPathsUtil(i, j - 1, k - 1, not d)
    return dp[i][j][k][d]


# This function mainly initializes 'dp' array
# as -1 and calls countPathsUtil()
def countPaths(i, j, k):
    # If (0, 0) is target itself
    if (i == 0 and j == 0):
        return 1

    # Recur for two cases: moving along row
    # and along column
    return countPathsUtil(i - 1, j, k, 1) + \
           countPathsUtil(i, j - 1, k, 0)


# Driver Code
if __name__ == '__main__':
    m = 3
    n = 3
    k = 2
    print("Number of paths is",countPaths(m - 1, n - 1, k))
