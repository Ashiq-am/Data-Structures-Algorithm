# An Not in-place Python program
# to reverse an array

''' Function to reverse arr[]
	from start to end '''


def revereseArray(arr, n):
    # Create a copy array
    # and store reversed
    # elements
    rev = n * [0]
    for i in range(0, n):
        rev[n - i - 1] = arr[i]

    # Now copy reversed
    # elements back to arr[]
    for i in range(0, n):
        arr[i] = rev[i]


# Driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    n = len(arr)
    print(*arr)
    revereseArray(arr, n)
    print("Reversed array is")
    print(*arr)


