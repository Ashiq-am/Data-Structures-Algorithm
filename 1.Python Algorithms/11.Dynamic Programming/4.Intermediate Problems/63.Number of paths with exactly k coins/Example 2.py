# A Dynamic Programming based Python3 program to
# count paths with exactly 'k' coins
R = 3
C = 3
MAX_K = 1000


def pathCountDPRecDP(mat, m, n, k):
    # Base cases
    if m < 0 or n < 0:
        return 0
    elif m == 0 and n == 0:
        return k == mat[m][n]

    # If this subproblem is already solved
    if (dp[m][n][k] != -1):
        return dp[m][n][k]

    # #(m, n) can be reached either
    # through (m-1, n) or through
    # (m, n-1)
    dp[m][n][k] = (pathCountDPRecDP(mat, m - 1, n, k - mat[m][n]) +
                   pathCountDPRecDP(mat, m, n - 1, k - mat[m][n]))

    return dp[m][n][k]


# A wrapper over pathCountDPRecDP()
def pathCountDP(mat, k):
    return pathCountDPRecDP(mat, R - 1, C - 1, k)


# Driver Code
k = 12

# Initialising dp[][][]
dp = [[[-1 for col in range(MAX_K)]
       for col in range(C)]
      for row in range(R)]

mat = [[1, 2, 3],
       [4, 6, 5],
       [3, 2, 1]]

print(pathCountDP(mat, k))
