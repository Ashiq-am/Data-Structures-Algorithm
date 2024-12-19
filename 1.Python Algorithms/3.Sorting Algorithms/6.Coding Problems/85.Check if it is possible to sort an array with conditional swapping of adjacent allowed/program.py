# Python 3 program to
# check if we can sort
# an array with adjacent
# swaps allowed

# Returns true if it
# is possible to sort
# else false/
def checkForSorting(arr, n):
    for i in range(0, n - 1):

        # We need to do something only if
        # previousl element is greater
        if (arr[i] > arr[i + 1]):

            if (arr[i] - arr[i + 1] == 1):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

            # If difference is more than
            # one, then not possible
            else:
                return False

    return True


# Driver code
arr = [1, 0, 3, 2]
n = len(arr)
if (checkForSorting(arr, n)):
    print("Yes")
else:
    print("No")
