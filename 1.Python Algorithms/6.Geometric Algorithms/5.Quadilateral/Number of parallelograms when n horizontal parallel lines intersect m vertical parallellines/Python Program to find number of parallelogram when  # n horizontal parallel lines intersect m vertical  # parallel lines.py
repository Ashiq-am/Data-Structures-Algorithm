# Python Program to find number of parallelogram when
# n horizontal parallel lines intersect m vertical
# parallel lines.
MAX = 10


# Find value of Binomial Coefficient
def binomialCoeff(C, n, k):
    # Calculate value of Binomial Coefficient
    # in bottom up manner
    for i in range(n + 1):
        for j in range(0, min(i, k) + 1):

            # Base Cases
            if (j == 0 or j == i):
                C[i][j] = 1

            # Calculate value using previously
            # stored values
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

            # Return number of parallelogram when n horizontal


# parallel lines intersect m vertical parallel lines.
def countParallelogram(n, m):
    C = [[0 for i in range(MAX)] for j in range(MAX)]

    binomialCoeff(C, max(n, m), 2)

    return C[n][2] * C[m][2]


# Driver code
if __name__ == '__main__':
    n = 5
    m = 5
    print(countParallelogram(n, m))
