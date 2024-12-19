# Python3 program to count of 6 values
# from an array that satisfy an equation
# with 6 variables

def upper_bound(array, length, value):
    low = 0
    high = length
    while (low < high):
        mid = int((low + high) / 2)
        if (value >= array[mid]):
            low = mid + 1
        else:
            high = mid

    return low


def lower_bound(array, length, value):
    low = 0
    high = length
    while (low < high):
        mid = int((low + high) / 2)
        if (value <= array[mid]):
            high = mid
        else:
            low = mid + 1
    return low


def findSextuplets(arr, n):
    # Generating possible values of
    # RHS of the equation
    index = 0
    RHS = [0] * (n * n * n + 1)

    for i in range(n):
        if (arr[i] != 0):

            # Checking d should be non-zero.
            for j in range(n):
                for k in range(n):
                    RHS[index] = arr[i] * (arr[j] + arr[k])
                    index += 1

    # Sort RHS[] so that we can do
    # binary search in it.
    RHS.sort()

    # Generating all possible values of
    # LHS of the equation and finding the
    # number of occurances of the value in RHS.
    result = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                val = arr[i] * arr[j] + arr[k]
                result += (upper_bound(RHS, index, val) - lower_bound(RHS, index, val))

    return result


# Driver Code
arr = [2, 3]
n = len(arr)

print(findSextuplets(arr, n))

