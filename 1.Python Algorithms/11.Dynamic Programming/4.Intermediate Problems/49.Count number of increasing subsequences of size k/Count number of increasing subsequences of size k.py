# Python3 implementation to count number
# of increasing subsequences of size k
import math as mt


# function to count number of increasing
# subsequences of size k
def numOfIncSubseqOfSizeK(arr, n, k):
    dp = [[0 for i in range(n)]
          for i in range(k)]

    # count of increasing subsequences
    # of size 1 ending at each arr[i]
    for i in range(n):
        dp[0][i] = 1

    # building up the matrix dp[][]
    # Here 'l' signifies the size of
    # increasing subsequence of size (l+1).
    for l in range(1, k):

        # for each increasing subsequence of
        # size 'l' ending with element arr[i]
        for i in range(l, n):

            # count of increasing subsequences of
            # size 'l' ending with element arr[i]
            dp[l][i] = 0
            for j in range(l - 1, i):
                if (arr[j] < arr[i]):
                    dp[l][i] += dp[l - 1][j]

    # Sum up the count of increasing subsequences
    # of size 'k' ending at each element arr[i]
    Sum = 0
    for i in range(k - 1, n):
        Sum += dp[k - 1][i]

    # required number of increasing
    # subsequences of size k
    return Sum


# Driver Code
arr = [12, 8, 11, 13, 10,
       15, 14, 16, 20]
n = len(arr)
k = 4

print("Number of Increasing Subsequences of size",k, "=", numOfIncSubseqOfSizeK(arr, n, k))


