# Python3 Program to find Entringer
# Number E(n, k)

# Return Entringer Number E(n, k)
def zigzag(n, k):
    dp = [[0 for x in range(k + 1)]
          for y in range(n + 1)]

    # Base cases
    dp[0][0] = 1
    for i in range(1, n + 1):
        dp[i][0] = 0

    # Finding dp[i][j]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = (dp[i][j - 1]
                        + dp[i - 1][i - j])

    return dp[n][k]


# Driven Program
n = 4
k = 3
print(zigzag(n, k))



