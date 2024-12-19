# Python3 program to count ways to build
# street under given constraints

# function to count ways of building
# a street of n rows
def countWays(n):
    dp = [[0] * (n + 1) for i in range(2)]

    # base case
    dp[0][1] = 1
    dp[1][1] = 2

    for i in range(2, n + 1):
        # ways of building houses in both
        # the spots of ith row
        dp[0][i] = dp[0][i - 1] + dp[1][i - 1]

        # ways of building an office in one of
        # the two spots of ith row
        dp[1][i] = (dp[0][i - 1] * 2 +
                    dp[1][i - 1])

    # total ways for n rows
    return dp[0][n] + dp[1][n]


# Driver Code
if __name__ == "__main__":
    n = 5
    print("Total no of ways with n =",n, "are:", countWays(n))
