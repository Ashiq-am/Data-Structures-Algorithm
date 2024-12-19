# Python program to get index of array element in
# sorted array
# Method returns the position of arr[idx] after
# performing stable-sort on array

def getIndexInSortedArray(arr, n, idx):
	# Count of elements smaller than current
	# element plus the equal element occurring
	# before given index
	result = 0
	for i in range(n):
		# If element is smaller then increase
		# the smaller count
		if (arr[i] < arr[idx]):
			result += 1

		# If element is equal then increase count
		# only if it occurs before
		if (arr[i] == arr[idx] and i < idx):
			result += 1
	return result

# Driver code to test above methods
arr = [3, 4, 3, 5, 2, 3, 4, 3, 1, 5]
n = len(arr)

idxOfEle = 5
print(getIndexInSortedArray(arr, n, idxOfEle))


