# DP based Python 3 program to find n-th
# Rencontres Number

MAX = 100


# Fills table C[n+1][k+1] such that C[i][j]
# represents table of binomial coefficient
# iCj
def binomialCoeff(C, n, k):
    # Calculate value of Binomial Coefficient
    # in bottom up manner
    for i in range(0, n + 1):
        for j in range(0, min(i, k) + 1):

            # Base Cases
            if (j == 0 or j == i):
                C[i][j] = 1

            # Calculate value using previously
            # stored values
            else:
                C[i][j] = (C[i - 1][j - 1]
                           + C[i - 1][j])


# Return Recontres number D(n, m)
def RencontresNumber(C, n, m):
    w, h = m + 1, n + 1
    dp = [[0 for x in range(w)] for y in range(h)]

    for i in range(0, n + 1):
        for j in range(0, m + 1):
            if (j <= i):

                # base case
                if (i == 0 and j == 0):
                    dp[i][j] = 1

                # base case
                elif (i == 1 and j == 0):
                    dp[i][j] = 0

                elif (j == 0):
                    dp[i][j] = ((i - 1) *
                                (dp[i - 1][0] + dp[i - 2][0]))
                else:
                    dp[i][j] = C[i][j] * dp[i - j][0]

    return dp[n][m]


# Driver Program
n = 7
m = 2
C = [[0 for x in range(MAX)] for y in range(MAX)]

binomialCoeff(C, n, m)

print(RencontresNumber(C, n, m))
