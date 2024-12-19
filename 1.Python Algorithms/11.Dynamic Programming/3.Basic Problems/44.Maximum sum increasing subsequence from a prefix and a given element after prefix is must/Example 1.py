# Python3 program to find maximum
# sum increasing subsequence till
# i-th index and including k-th index.

def pre_compute(a, n, index, k):
    dp = [[0 for i in range(n)]
          for i in range(n)]

    # Initializing the first
    # row of the dp[][]
    for i in range(n):
        if a[i] > a[0]:
            dp[0][i] = a[i] + a[0]
        else:
            dp[0][i] = a[i]

    # Creating the dp[][] matrix.
    for i in range(1, n):
        for j in range(n):
            if a[j] > a[i] and j > i:
                if dp[i - 1][i] + a[j] > dp[i - 1][j]:
                    dp[i][j] = dp[i - 1][i] + a[j]
                else:
                    dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    # To calculate for i=4 and k=6.
    return dp[index][k]


# Driver code
a = [1, 101, 2, 3, 100, 4, 5]
n = len(a)
index = 4
k = 6
print(pre_compute(a, n, index, k))
