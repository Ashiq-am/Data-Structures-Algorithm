# A Dynamic Programming based Python3 program
# to count number of partitions of a set with
# n elements into k subsets

# Returns count of different partitions
# of n elements in k subsets
def countP(n, k):
    # Table to store results of subproblems
    dp = [[0 for i in range(k + 1)]
          for j in range(n + 1)]

    # Base cases
    for i in range(n + 1):
        dp[i][0] = 0

    for i in range(k + 1):
        dp[0][k] = 0

    # Fill rest of the entries in
    # dp[][] in bottom up manner
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if (j == 1 or i == j):
                dp[i][j] = 1
            else:
                dp[i][j] = (j * dp[i - 1][j] +
                            dp[i - 1][j - 1])

    return dp[n][k]


# Driver Code
if __name__ == '__main__':
    print(countP(5, 2))
