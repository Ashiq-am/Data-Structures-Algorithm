# Python implementation of the above approach

def RearrangePosNeg(arr, n):
    i = 0
    j = n - 1

    while (True):
        # Loop until arr[i] < 0 and
        # still inside the array
        while (arr[i] < 0 and i < n):
            i += 1

        # Loop until arr[j] > 0 and
        # still inside the array
        while (arr[j] > 0 and j >= 0):
            j -= 1
        # if i is less than j
        if (i < j):
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break


# Driver Code
arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
n = len(arr)
RearrangePosNeg(arr, n)
print(*arr)
