# Python3 program to find minimum
# adjustment cost of an array
M = 100


# Function to find minimum
# adjustment cost of an array
def minAdjustmentCost(A, n, target):
    # dp[i][j] stores minimal adjustment
    # cost on changing A[i] to j
    dp = [[0 for i in range(M + 1)]
          for i in range(n)]

    # handle first element
    # of array separately
    for j in range(M + 1):
        dp[0][j] = abs(j - A[0])

    # do for rest elements
    # of the array
    for i in range(1, n):

        # replace A[i] to j and
        # calculate minimal adjustment
        # cost dp[i][j]
        for j in range(M + 1):

            # initialize minimal adjustment
            # cost to INT_MAX
            dp[i][j] = 100000000

            # consider all k such that
            # k >= max(j - target, 0) and
            # k <= min(M, j + target) and
            # take minimum
            for k in range(max(j - target, 0),
                           min(M, j + target) + 1):
                dp[i][j] = min(dp[i][j], dp[i - 1][k] +
                               abs(A[i] - j))

    # return minimum value from
    # last row of dp table
    res = 10000000
    for j in range(M + 1):
        res = min(res, dp[n - 1][j])
    return res


# Driver Code
arr = [55, 77, 52, 61, 39,
       6, 25, 60, 49, 47]
n = len(arr)
target = 10
print("Minimum adjustment cost is",
      minAdjustmentCost(arr, n, target),
      sep=' ')
