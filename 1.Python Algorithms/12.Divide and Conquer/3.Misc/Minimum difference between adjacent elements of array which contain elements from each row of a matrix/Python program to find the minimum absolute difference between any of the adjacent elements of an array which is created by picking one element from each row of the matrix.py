# Python program to find the minimum absolute difference
# between any of the adjacent elements of an array
# which is created by picking one element from each
# row of the matrix.
# R 2
# C 2

# Return smallest element greater than or equal
# to the current element.
def bsearch(low, high, n, arr):
	mid = (low + high)/2

	if(low <= high):
		if(arr[mid] < n):
			return bsearch(mid +1, high, n, arr);
		return bsearch(low, mid - 1, n, arr);

	return low;

# Return the minimum absolute difference adjacent
# elements of array
def mindiff(arr, n, m):

	# arr = [0 for i in range(R)][for j in range(C)]
	# Sort each row of the matrix.
	for i in range(n):
		sorted(arr)

	ans = 2147483647

	# For each matrix element
	for i in range(n-1):
		for j in range(m):
			# Search smallest element in the next row which
			# is greater than or equal to the current element
			p = bsearch(0, m-1, arr[i][j], arr[i + 1])
			ans = min(ans, abs(arr[i + 1][p] - arr[i][j]))

			# largest element which is smaller than the current
			# element in the next row must be just before
			# smallest element which is greater than or equal
			# to the current element because rows are sorted.
			if (p-1 >= 0):
				ans = min(ans, abs(arr[i + 1][p - 1] - arr[i][j]))
	return ans;

# Driver Program
m =[8, 5], [6, 8]
print(mindiff(m, 2, 2))


