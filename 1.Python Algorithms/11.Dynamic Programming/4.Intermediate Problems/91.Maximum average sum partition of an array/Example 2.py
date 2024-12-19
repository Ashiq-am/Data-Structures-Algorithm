# Python3 program for maximum average
# sum partition
def largestSumOfAverages(A, K):
    n = len(A)

    # storing prefix sums
    pre_sum = [0] * (n + 1)
    pre_sum[0] = 0
    for i in range(n):
        pre_sum[i + 1] = pre_sum[i] + A[i]

    # for each i to n storing averages
    dp = [0] * n
    sum = 0
    for i in range(n):
        dp[i] = (pre_sum[n] -
                 pre_sum[i]) / (n - i)

    for k in range(K - 1):
        for i in range(n):
            for j in range(i + 1, n):
                dp[i] = max(dp[i],(pre_sum[j] - pre_sum[i]) / (j - i) + dp[j])

    return int(dp[0])


# Driver code
A = [9, 1, 2, 3, 9]
K = 3  # atmost partitioning size
print(largestSumOfAverages(A, K))


