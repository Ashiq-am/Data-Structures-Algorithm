# Python3 program to get sum
# of average of all subsets

# Returns value of Binomial
# Coefficient C(n, k)
def nCr(n, k):
    C = [[0 for i in range(k + 1)]
         for j in range(n + 1)]

    # Calculate value of Binomial
    # Coefficient in bottom up manner
    for i in range(n + 1):

        for j in range(min(i, k) + 1):

            # Base Cases
            if (j == 0 or j == i):
                C[i][j] = 1

            # Calculate value using
            # previously stored values
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

    return C[n][k]


# Method returns sum of
# average of all subsets
def resultOfAllSubsets(arr, N):
    result = 0.0  # Initialize result

    # Find sum of elements
    sum = 0
    for i in range(N):
        sum += arr[i]

    # looping once for all subset of same size
    for n in range(1, N + 1):
        # each element occurs nCr(N-1, n-1) times while
        # considering subset of size n */
        result += (sum * (nCr(N - 1, n - 1))) / n

    return result


# Driver code
arr = [2, 3, 5, 7]
N = len(arr)
print(resultOfAllSubsets(arr, N))
