# Python3 program to find number of ways
# to arrange items under given constraint
import numpy as np


# method returns number of ways with
# which items can be arranged
def waysToArrange(N, K, k):
    C = np.zeros((N + 1, N + 1))

    # Calculate value of Binomial
    # Coefficient in bottom up manner
    for i in range(N + 1):
        for j in range(i + 1):

            # Base Cases
            if (j == 0 or j == i):
                C[i][j] = 1

            # Calculate value using previously
            # stored values
            else:
                C[i][j] = (C[i - 1][j - 1] +
                           C[i - 1][j])

    # declare dp array to store result
    # up to ith colored item
    dp = np.zeros((K + 1))

    # variable to keep track of count
    # of items considered till now
    count = 0

    dp[0] = 1

    # loop over all different colors
    for i in range(K):
        # populate next value using current
        # value and stated relation
        dp[i + 1] = (dp[i] * C[count + k[i] - 1][k[i] - 1])
        count += k[i]

    # return value stored at last index
    return dp[K]


# Driver code
if __name__ == "__main__":
    N = 4
    k = [2, 2]

    K = len(k)
    print(int(waysToArrange(N, K, k)))
