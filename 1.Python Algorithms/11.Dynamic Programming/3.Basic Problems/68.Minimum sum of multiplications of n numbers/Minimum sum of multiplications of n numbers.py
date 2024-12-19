# Python3 program to find the
# minimum sum of multiplication
# of n numbers

import numpy as np
import sys

# Used in recursive
# memoized solution
dp = np.zeros((1000, 1000))


# function to calculate the cumulative
# sum from a[i] to a[j]
def sum(a, i, j):
    ans = 0
    for m in range(i, j + 1):
        ans = (ans + a[m]) % 100

    return ans


def solve(a, i, j):
    # base case
    if (i == j):
        return 0

    # memoization, if the partition
    # has been called before then
    # return the stored value
    if (dp[i][j] != -1):
        return dp[i][j]

    # store a max value
    dp[i][j] = sys.maxsize

    # we break them into k partitions
    for k in range(i, j):
        # store the min of the
        # formula thus obtained
        dp[i][j] = min(dp[i][j], (solve(a, i, k) + solve(a, k + 1, j)
                                  + (sum(a, i, k) * sum(a, k + 1, j))))

    # return the minimum
    return dp[i][j]


def initialize(n):
    for i in range(n + 1):
        for j in range(n + 1):
            dp[i][j] = -1


# Driver code
if __name__ == "__main__":
    a = [40, 60, 20]
    n = len(a)
    initialize(n)
    print(int(solve(a, 0, n - 1)))
