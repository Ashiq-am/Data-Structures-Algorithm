# Python implementation
# to divide N into maximum
# number of segments of
# length a, b and c

# function to find
# the maximum number
# of segments
def maximumSegments(n, a, b, c):
    # stores the maximum
    # number of segments
    # each index can have
    dp = [-1] * (n + 10)

    # 0th index will have
    # 0 segments base case
    dp[0] = 0

    # traverse for all possible
    # segments till n
    for i in range(0, n):

        if (dp[i] != -1):

            # conditions
            if (i + a <= n):  # avoid buffer overflow
                dp[i + a] = max(dp[i] + 1,
                                dp[i + a])

            if (i + b <= n):  # avoid buffer overflow
                dp[i + b] = max(dp[i] + 1,
                                dp[i + b])

            if (i + c <= n):  # avoid buffer overflow
                dp[i + c] = max(dp[i] + 1,
                                dp[i + c])

    return dp[n]


# Driver code
n = 7
a = 5
b = 2
c = 5
print(maximumSegments(n, a, b, c))
