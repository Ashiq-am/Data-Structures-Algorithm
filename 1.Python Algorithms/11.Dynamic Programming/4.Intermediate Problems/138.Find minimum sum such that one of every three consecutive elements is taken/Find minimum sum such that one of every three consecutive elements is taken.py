# A Dynamic Programming based python 3 program to
# find minimum possible sum of elements of array
# such that an element out of every three
# consecutive is picked.

# A utility function to find minimum of
# 3 elements
def minimum(a, b, c):
    return min(min(a, b), c);


# Returns minimum possible sum of elements such
# that an element out of every three consecutive
# elements is picked.
def findMinSum(arr, n):
    # Create a DP table to store results of
    # subproblems. sum[i] is going to store
    # minimum possible sum when arr[i] is
    # part of the solution.
    sum = []

    # When there are less than or equal to
    # 3 elements
    sum.append(arr[0])
    sum.append(arr[1])
    sum.append(arr[2])

    # Iterate through all other elements
    for i in range(3, n):
        sum.append(arr[i] + minimum(sum[i - 3],
                                    sum[i - 2], sum[i - 1]))

    return minimum(sum[n - 1], sum[n - 2], sum[n - 3])


# Driver code
arr = [1, 2, 3, 20, 2, 10, 1]
n = len(arr)
print("Min Sum is ", findMinSum(arr, n))
