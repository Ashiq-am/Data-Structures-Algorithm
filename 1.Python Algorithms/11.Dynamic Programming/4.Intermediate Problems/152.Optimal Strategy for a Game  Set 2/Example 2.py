# Python3 program to find out maximum value
# from a given sequence of coins
MAX = 100

memo = [[0 for i in range(MAX)]
        for j in range(MAX)]


def oSRec(arr, i, j, Sum):
    if (j == i + 1):
        return max(arr[i], arr[j])

    if (memo[i][j] != -1):
        return memo[i][j]

    # For both of your choices, the opponent
    # gives you total sum minus maximum of
    # his value
    memo[i][j] = max((Sum - oSRec(arr, i + 1, j,
                                  Sum - arr[i])),
                     (Sum - oSRec(arr, i, j - 1,
                                  Sum - arr[j])))

    return memo[i][j]


# Returns optimal value possible that a
# player can collect from an array of
# coins of size n. Note than n must
# be even
def optimalStrategyOfGame(arr, n):
    # Compute sum of elements
    Sum = 0
    Sum = sum(arr)

    # Initialize memoization table
    for j in range(MAX):
        for k in range(MAX):
            memo[j][k] = -1

    return oSRec(arr, 0, n - 1, Sum)


# Driver Code
arr1 = [8, 15, 3, 7]
n = len(arr1)
print(optimalStrategyOfGame(arr1, n))

arr2 = [2, 2, 2, 2]
n = len(arr2)
print(optimalStrategyOfGame(arr2, n))

arr3 = [20, 30, 2, 2, 2, 10]
n = len(arr3)
print(optimalStrategyOfGame(arr3, n))
