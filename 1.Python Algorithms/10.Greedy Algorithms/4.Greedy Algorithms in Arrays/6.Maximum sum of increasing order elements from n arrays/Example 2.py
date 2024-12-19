# Python3 program to find maximum sum
# by selecting a element from n arrays
M = 4

# To calculate maximum sum by
# selecting element from each array
def maximumSum(a, n):

	# Store maximum element of last array
	prev = max(max(a))

	# Selecting maximum element from
	# previoulsy selected element
	Sum = prev
	for i in range(n - 2, -1, -1):

		max_smaller = -10**9
		for j in range(M - 1, -1, -1):
			if (a[i][j] < prev and
				a[i][j] > max_smaller):
				max_smaller = a[i][j]

	# max_smaller equals to INT_MIN means
	# no element is found in a[i] so
	# return 0
		if (max_smaller == -10**9):
			return 0

		prev = max_smaller
		Sum += max_smaller

	return Sum

# Driver Code
arr = [[1, 7, 3, 4],
	[4, 2, 5, 1],
	[9, 5, 1, 8]]
n = len(arr)
print(maximumSum(arr, n))
