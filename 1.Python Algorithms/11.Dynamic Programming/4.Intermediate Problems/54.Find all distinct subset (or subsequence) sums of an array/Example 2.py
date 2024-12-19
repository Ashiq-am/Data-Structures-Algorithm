# Python3 program to prdistinct subset
# Sums of a given array.

# Uses Dynamic Programming to find
# distinct subset Sums
def printDistSum(arr, n):
    Sum = sum(arr)

    # dp[i][j] would be true if arr[0..i-1]
    # has a subset with Sum equal to j.
    dp = [[False for i in range(Sum + 1)]
          for i in range(n + 1)]

    # There is always a subset with 0 Sum
    for i in range(n + 1):
        dp[i][0] = True

    # Fill dp[][] in bottom up manner
    for i in range(1, n + 1):

        dp[i][arr[i - 1]] = True

        for j in range(1, Sum + 1):

            # Sums that were achievable
            # without current array element
            if (dp[i - 1][j] == True):
                dp[i][j] = True
                dp[i][j + arr[i - 1]] = True

    # Print last row elements
    for j in range(Sum + 1):
        if (dp[n][j] == True):
            print(j, end=" ")


# Driver code
arr = [2, 3, 4, 5, 6]
n = len(arr)
printDistSum(arr, n)

