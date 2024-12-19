# Python 3 implementation of the approach

# Linearly search x in arr[]. If x is present
# then return the index, otherwise return -1


def search(arr, x):
	for index, value in enumerate(arr):
		if value == x:
			return index
	return -1


# Driver Code
arr = [1, 10, 30, 15]
x = 30
print(x, "is present at index",search(arr, x))
