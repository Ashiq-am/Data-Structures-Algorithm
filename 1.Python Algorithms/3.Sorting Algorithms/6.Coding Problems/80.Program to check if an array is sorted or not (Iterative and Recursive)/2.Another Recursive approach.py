# Python3 recursive program to check
# if an Array is sorted or not

# Function that returns true if array
# is sorted in non-decreasing order.
def arraySortedOrNot(arr, n):
    # Base case
    if (n == 0 or n == 1):
        return True

    # Check if present index and index
    # previous to it are in correct order
    # and rest of the array is also sorted
    # if true then return true else return
    # false
    return (arr[n - 1] >= arr[n - 2] and
            arraySortedOrNot(arr, n - 1))


# Driver code
arr = [20, 23, 23, 45, 78, 88]
n = len(arr)

# Function Call
if (arraySortedOrNot(arr, n)):
    print("Yes")
else:
    print("No")
