# Python program of Pancake Sorting Problem
# A Binary Search based function to get index of ceiling of x in arr[low..high]

def ceilSearch(arr, low, high, x):
    # If x is smaller than or equal to the first element,
    # then return the first element
    if x <= arr[low]:
        return low

    # If x is greater than the last element, then return -1
    if x > arr[high]:
        return -1

    # get the index of middle element of arr[low..high]
    mid = (low + high) / 2  # low + (high-low)/2

    # If x is same as middle element, then return mid
    if (arr[mid] == x):
        return mid

    # If x is greater than arr[mid], then either arr[mid + 1]
    # is ceiling of x, or ceiling lies in arr[mid+1...high]
    if (arr[mid] < x):
        if (mid + 1 <= high and x <= arr[mid + 1]):
            return mid + 1
        else:
            return ceilSearch(arr, mid + 1, high, x)

    # If x is smaller than arr[mid], then either arr[mid]
    # is ceiling of x or ceiling lies in arr[mid-1...high]
    if (mid - 1 >= low and x > arr[mid - 1]):
        return mid
    else:
        return ceilSearch(arr, low, mid - 1, x)


# Reverses arr[0..i] */
def flip(arr, i):
    start = 0
    while (start < i):
        temp = arr[start]
        arr[start] = arr[i]
        arr[i] = temp
        start += 1
        i -= 1


# Function to sort an array using insertion sort, binary search and flip
def insertionSort(arr):
    # Start from the second element and one by one insert arr[i]
    # in already sorted arr[0..i-1]
    for i in range(1, len(arr)):
        # Find the smallest element in arr[0..i-1] which is also greater than
        # or equal to arr[i]
        j = ceilSearch(arr, 0, i - 1, arr[i])

        # Check if there was no element greater than arr[i]
        if (j != -1):
            # Put arr[i] before arr[j] using following four flip operations
            flip(arr, j - 1)
            flip(arr, i - 1)
            flip(arr, i)
            flip(arr, j)


# A utility function to print an array of size n
def printArray(arr):
    for i in range(0, len(arr)):
        print(arr[i])


# Driver function to test above function
arr = [18, 40, 35, 12, 30, 35, 20, 6, 90, 80]
insertionSort(arr)
printArray(arr)
