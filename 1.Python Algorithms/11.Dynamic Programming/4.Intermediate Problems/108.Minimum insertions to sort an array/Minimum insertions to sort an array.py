# Python3 program to get minimum number
# of insertion steps to sort an array

# method returns min steps of insertion
# we need to perform to sort array 'arr'
def minInsertionStepToSortArray(arr, N):

	# lis[i] is going to store length
	# of lis that ends with i.
	lis = [0] * N

	# Initialize lis values for all indexes
	for i in range(N):
		lis[i] = 1

	# Compute optimized lis values in
	# bottom up manner
	for i in range(1, N):
		for j in range(i):
			if (arr[i] >= arr[j] and
				lis[i] < lis[j] + 1):
				lis[i] = lis[j] + 1

	# The overall LIS must end with of the array
	# elements. Pick maximum of all lis values
	max = 0
	for i in range(N):
		if (max < lis[i]):
			max = lis[i]

	# return size of array minus length
	# of LIS as final result
	return (N - max)

# Driver Code
if __name__ == "__main__":
	arr = [2, 3, 5, 1, 4, 7, 6]
	N = len(arr)
	print (minInsertionStepToSortArray(arr, N))
