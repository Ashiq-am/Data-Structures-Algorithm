# Python3 program to sort an
# array according absolute
# difference with x.

# Function to sort an array
# according absolute difference
# with x.
def rearrange(arr, n, x):
    m = {}

    # Store values in a map
    # with the difference
    # with X as key
    for i in range(n):
        m[arr[i]] = abs(x - arr[i])

    m = {k: v for k, v in sorted(m.items(),
                                 key=lambda item: item[1])}

    # Update the values of array
    i = 0

    for it in m.keys():
        arr[i] = it
        i += 1


# Function to print the array
def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")


# Driver code
if __name__ == "__main__":
    arr = [10, 5, 3, 9, 2]
    n = len(arr)
    x = 7
    rearrange(arr, n, x)
    printArray(arr, n)
