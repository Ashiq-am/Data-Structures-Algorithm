# Python3 program of above approach

# A utility function to find
# minimum in arr[l..h]
def min1(arr, l, h):
    mn = arr[l]
    for i in range(l + 1, h + 1):
        if (mn > arr[i]):
            mn = arr[i]
    return mn


# A utility function to find
# maximum in arr[l..h]
def max1(arr, l, h):
    mx = arr[l]
    for i in range(l + 1, h + 1):
        if (mx < arr[i]):
            mx = arr[i]
    return mx


# Returns the minimum number of removals
# from either end in arr[l..h] so that
# 2*min becomes greater than max.
def minRemovalsDP(arr, n):
    # Create a table to store
    # solutions of subproblems
    table = [[0 for x in range(n)] for y in range(n)]

    # Fill table using above recursive formula.
    # Note that the table is filled in diagonal fashion
    # (similar to http:#goo.gl/PQqoS), from diagonal elements
    # to table[0][n-1] which is the result.
    for gap in range(n):
        i = 0
        for j in range(gap, n):
            mn = min1(arr, i, j)
            mx = max1(arr, i, j)
            table[i][j] = 0 if (2 * mn > mx) else min(table[i][j - 1] + 1, table[i + 1][j] + 1)
            i += 1
    return table[0][n - 1]


# Driver Code
arr = [20, 4, 1, 3]
n = len(arr)
print(minRemovalsDP(arr, n))


