# Python3 program to count the number of
# arrays of size n such that every element is
# in range [1, m] and adjacent are divisible

MAX = 1000


def numofArray(n, m):
    dp = [[0 for i in range(MAX)] for j in range(MAX)]

    # For storing factors.
    di = [[] for i in range(MAX)]

    # For storing multiples.
    mu = [[] for i in range(MAX)]

    # calculating the factors and multiples
    # of elements [1...m].
    for i in range(1, m + 1):

        for j in range(2 * i, m + 1, i):
            di[j].append(i)
            mu[i].append(j)

        di[i].append(i)

    # Initialising for size 1 array for each i <= m.
    for i in range(1, m + 1):
        dp[1][i] = 1

    # Calculating the number of array possible
    # of size i and starting with j.
    for i in range(2, n + 1):

        for j in range(1, m + 1):

            dp[i][j] = 0

            # For all previous possible values.
            # Adding number of factors.
            for x in di[j]:
                dp[i][j] += dp[i - 1][x]

            # Adding number of multiple.
            for x in mu[j]:
                dp[i][j] += dp[i - 1][x]

    # Calculating the total count of array
    # which start from [1...m].
    ans = 0
    for i in range(1, m + 1):
        ans += dp[n][i]
        di[i].clear()
        mu[i].clear()

    return ans


# Driven Program
if __name__ == "__main__":
    n = m = 3
    print(numofArray(n, m))

# This code is contributed by Rituraj Jain
