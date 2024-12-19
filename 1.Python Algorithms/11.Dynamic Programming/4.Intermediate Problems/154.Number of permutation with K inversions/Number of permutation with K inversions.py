# Python3 program to find number of permutation
# with K inversion using Memoization

# Limit on N and K
M = 100

# 2D array memo for stopping
# solving same problem again
memo = [[0 for i in range(M)] for j in range(M)]


# method recursively calculates
# permutation with K inversion
def numberOfPermWithKInversion(N, K):
    # Base cases
    if (N == 0): return 0
    if (K == 0): return 1

    # If already solved then
    # return result directly
    if (memo[N][K] != 0):
        return memo[N][K]

    # Calling recursively all subproblem
    # of permutation size N - 1
    sum = 0
    for i in range(K + 1):

        # Call recursively only if
        # total inversion to be made
        # are less than size
        if (i <= N - 1):
            sum += numberOfPermWithKInversion(N - 1, K - i)

    # store result into memo
    memo[N][K] = sum

    return sum


# Driver code
N = 4
K = 2
print(numberOfPermWithKInversion(N, K))
