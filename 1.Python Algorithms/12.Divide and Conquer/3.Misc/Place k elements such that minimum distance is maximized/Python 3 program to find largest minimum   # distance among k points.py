# Python 3 program to find largest minimum
# distance among k points.

# Returns true if it is possible to arrange
# k elements of arr[0..n-1] with minimum
# distance given as mid.
def isFeasible(mid, arr, n, k):
    # Place first element at arr[0] position
    pos = arr[0]

    # Initialize count of elements placed.
    elements = 1

    # Try placing k elements with minimum
    # distance mid.
    for i in range(1, n, 1):
        if (arr[i] - pos >= mid):

            # Place next element if its distance
            # from the previously placed element
            # is greater than current mid
            pos = arr[i]
            elements += 1

            # Return if all elements are placed
            # successfully
            if (elements == k):
                return True
    return 0


# Returns largest minimum distance for k elements
# in arr[0..n-1]. If elements can't be placed,
# returns -1.
def largestMinDist(arr, n, k):
    # Sort the positions
    arr.sort(reverse=False)

    # Initialize result.
    res = -1

    # Consider the maximum possible distance
    left = arr[0]
    right = arr[n - 1]

    # Do binary search for largest
    # minimum distance
    while (left < right):
        mid = (left + right) / 2

        # If it is possible to place k elements
        # with minimum distance mid, search for
        # higher distance.
        if (isFeasible(mid, arr, n, k)):

            # Change value of variable max to mid iff
            # all elements can be successfully placed
            res = max(res, mid)
            left = mid + 1

        # If not possible to place k elements,
        # search for lower distance
        else:
            right = mid

    return res


# Driver code
if __name__ == '__main__':
    arr = [1, 2, 8, 4, 9]
    n = len(arr)
    k = 3
    print(largestMinDist(arr, n, k))

# This code is contributed by
# Sanjit_prasad
