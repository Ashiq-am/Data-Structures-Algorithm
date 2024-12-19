# Python Program to find max
# subarray sum excluding some
# elements

# Function to check the element
# present in array B
INT_MIN = -2147483648


def isPresent(B, m, x):
	for i in range(0, m):
		if B[i] == x:
			return True
	return False

# Utility function for findMaxSubarraySum()
# with the following parameters
# A => Array A,
# B => Array B,
# n => Number of elements in Array A,
# m => Number of elements in Array B


def findMaxSubarraySumUtil(A, B, n, m):

	# set max_so_far to INT_MIN
	max_so_far = INT_MIN
	curr_max = 0
	for i in range(0, n):
		if isPresent(B, m, A[i]) == True:
			curr_max = 0
			continue

		# Proceed as in Kadane's Algorithm
		curr_max = max(A[i], curr_max + A[i])
		max_so_far = max(max_so_far, curr_max)
	return max_so_far

# Wrapper for findMaxSubarraySumUtil()


def findMaxSubarraySum(A, B, n, m):

	maxSubarraySum = findMaxSubarraySumUtil(A, B, n, m)

	# This case will occur when all
	# elements of A are present
	# in B, thus no subarray can be
	# formed
	if maxSubarraySum == INT_MIN:
		print('Maximum Subarray Sum cant be found')
	else:
		print('The Maximum Subarray Sum =',
			maxSubarraySum)


# Driver code
A = [3, 4, 5, -4, 6]
B = [1, 8, 5]
n = len(A)
m = len(B)

# Function call
findMaxSubarraySum(A, B, n, m)
