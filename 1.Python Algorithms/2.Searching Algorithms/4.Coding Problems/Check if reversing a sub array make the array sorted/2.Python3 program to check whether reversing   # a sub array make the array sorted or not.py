# Python3 program to check whether reversing
# a sub array make the array sorted or not
import math as mt


# Return True, if reversing the subarray
# will sort the array, else return False.
def checkReverse(arr, n):
    if (n == 1):
        return True

    # Find first increasing part
    i = 1
    for i in range(1, n):
        if arr[i - 1] < arr[i]:
            if (i == n):
                return True

        else:
            break

    # Find reversed part
    j = i
    while (j < n and arr[j] < arr[j - 1]):

        if (i > 1 and arr[j] < arr[i - 2]):
            return False
        j += 1

    if (j == n):
        return True

    # Find last increasing part
    k = j

    # To handle cases like 1,2,3,4,20,9,16,17
    if (arr[k] < arr[i - 1]):
        return False

    while (k > 1 and k < n):

        if (arr[k] < arr[k - 1]):
            return False
        k += 1

    return True


# Driver Code
arr = [1, 3, 4, 10, 9, 8]
n = len(arr)
if checkReverse(arr, n):
    print("Yes")
else:
    print("No")
