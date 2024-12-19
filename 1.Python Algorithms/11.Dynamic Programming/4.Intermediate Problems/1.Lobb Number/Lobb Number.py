# Python 3 Program to find Ln,
# m Lobb Number.

# Returns value of Binomial
# Coefficient C(n, k)
def binomialCoeff(n, k):
    C = [[0 for j in range(k + 1)]
         for i in range(n + 1)]

    # Calculate value of Binomial
    # Coefficient in bottom up manner
    for i in range(0, n + 1):
        for j in range(0, min(i, k) + 1):
            # Base Cases
            if (j == 0 or j == i):
                C[i][j] = 1

            # Calculate value using
            # previously stored values
            else:
                C[i][j] = (C[i - 1][j - 1]
                           + C[i - 1][j])

    return C[n][k]


# Return the Lm, n Lobb Number.
def lobb(n, m):
    return (((2 * m + 1) *
             binomialCoeff(2 * n, m + n))
            / (m + n + 1))


# Driven Program
n = 5
m = 3
print(int(lobb(n, m)))
