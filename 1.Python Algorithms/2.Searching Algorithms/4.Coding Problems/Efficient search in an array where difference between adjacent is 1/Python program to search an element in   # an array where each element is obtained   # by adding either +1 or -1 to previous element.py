# Python program to search an element in
# an array where each element is obtained
# by adding either +1 or -1 to previous element

# Return the index of the element to be searched
def search(arr, n, x):
    # Searching x in arr[0..n-1]
    i = 0
    while (i <= n - 1):

        # Checking if element is found.
        if (arr[i] == x):
            return i

        # Else jumping to abs(arr[i]-x).
        i += abs(arr[i] - x)

    return -1


# Driver code
arr = [5, 4, 5, 6, 5, 4, 3, 2]
n = len(arr)
x = 4

print(search(arr, n, x))
