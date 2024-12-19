# Python 3 program to find minimum
# increment/decrement operations to
# make array elements same.

def MinOperation(a, b, n):
    # sorting both arrays in ascending order
    a.sort(reverse=False)
    b.sort(reverse=False)

    # variable to store the final result
    result = 0

    # After sorting both arrays. Now each
    # array is in non-decreasing order.
    # Thus, we will now compare each element
    # of the array and do the increment or
    # decrement operation depending upon
    # the value of array b[].
    for i in range(0, n, 1):
        if (a[i] > b[i]):
            result = result + abs(a[i] - b[i])

        elif (a[i] < b[i]):
            result = result + abs(a[i] - b[i])

    return result


# Driver code
if __name__ == '__main__':
    a = [3, 1, 1]
    b = [1, 2, 2]
    n = len(a)
    print(MinOperation(a, b, n))
