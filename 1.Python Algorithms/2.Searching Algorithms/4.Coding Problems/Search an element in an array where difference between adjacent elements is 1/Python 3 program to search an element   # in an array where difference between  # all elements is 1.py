# Python 3 program to search an element
# in an array where difference between
# all elements is 1

# x is the element to be searched in
# arr[0..n-1]
def search(arr, n, x):
    # Traverse the given array starting
    # from leftmost element
    i = 0
    while (i < n):

        # If x is found at index i
        if (arr[i] == x):
            return i

        # Jump the difference between
        # current array element and x
        i = i + abs(arr[i] - x)

    print("number is not present!")
    return -1


# Driver program to test above function
arr = [8, 7, 6, 7, 6, 5, 4, 3, 2, 3, 4, 3]
n = len(arr)
x = 3
print("Element", x, " is present at index ",
      search(arr, n, 3))

