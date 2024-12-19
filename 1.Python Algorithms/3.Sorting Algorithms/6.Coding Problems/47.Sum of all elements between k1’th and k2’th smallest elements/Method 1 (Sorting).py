# Python program to find sum of
# all element between to K1'th and
# k2'th smallest elements in array

# Returns sum between two kth
# smallest element of array
def sumBetweenTwoKth(arr, n, k1, k2):

	# Sort the given array
	arr.sort()

	result = 0
	for i in range(k1, k2-1):
		result += arr[i]
	return result

# Driver code
arr = [ 20, 8, 22, 4, 12, 10, 14 ]
k1 = 3; k2 = 6
n = len(arr)
print(sumBetweenTwoKth(arr, n, k1, k2))
