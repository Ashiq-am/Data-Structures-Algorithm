# Python3 program to find
# maximum sum by selecting
# a element from n arrays
M = 4


# To calculate maximum sum
# by selecting element from
# each array
def maximumSum(a, n):
    global M

    # Sort each array
    for i in range(0, n):
        a[i].sort()

    # Store maximum element
    # of last array
    sum = a[n - 1][M - 1]
    prev = a[n - 1][M - 1]

    # Selecting maximum
    # element from previoulsy
    # selected element
    for i in range(n - 2,
                   -1, -1):

        for j in range(M - 1,
                       -1, -1):

            if (a[i][j] < prev):
                prev = a[i][j]
                sum += prev
                break

        # j = -1 means no element
        # is found in a[i] so
        # return 0
        if (j == -1):
            return 0
    return sum


# Driver Code
arr = [[1, 7, 3, 4],
       [4, 2, 5, 1],
       [9, 5, 1, 8]]
n = len(arr)
print(maximumSum(arr, n))


