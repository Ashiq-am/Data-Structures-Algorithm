# Python 3 code to find number of ways of
# arranging bracket with proper expressions
N = 1000


# function to calculate the number
# of proper bracket sequence
def arrangeBraces(n, pos, k):
    # hash array to mark the
    # positions of opening brackets
    h = [False for i in range(N)]

    # dp 2d array
    dp = [[0 for i in range(N)]
          for i in range(N)]

    # mark positions in hash array
    for i in range(k):
        h[pos[i]] = 1

    # first position marked as 1
    dp[0][0] = 1

    # iterate and formulate the recurrences
    for i in range(1, 2 * n + 1):
        for j in range(2 * n + 1):

            # if position has a opening bracket
            if (h[i]):
                if (j != 0):
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 0
            else:
                if (j != 0):
                    dp[i][j] = (dp[i - 1][j - 1] +
                                dp[i - 1][j + 1])
                else:
                    dp[i][j] = dp[i - 1][j + 1]

    # return answer
    return dp[2 * n][0]


# Driver Code
n = 3

# positions where opening braces
# will be placed
pos = [2, ]
k = len(pos)
print(arrangeBraces(n, pos, k))

