# Python3 Program for finding nth
# Delannoy Number.

# Return the nth Delannoy Number.
def dealnnoy(n, m):
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # Base cases
    for i in range(m):
        dp[0][i] = 1

    for i in range(1, m + 1):
        dp[i][0] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] + dp[i][j - 1];

    return dp[m][n]


# Driven code
n = 3
m = 4
print(dealnnoy(n, m))
