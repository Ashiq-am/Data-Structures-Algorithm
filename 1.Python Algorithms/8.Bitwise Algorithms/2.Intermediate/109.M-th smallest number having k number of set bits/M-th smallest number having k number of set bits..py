# Python3 implementation to find the mth
# smallest number having k number of set bits

# function to find the next higher number
# with same number of set bits as in 'x'


def nxtHighWithNumOfSetBits(x):
	rightOne = 0
	nextHigherOneBit = 0
	rightOnesPattern = 0

	next = 0

	""" the approach is same as discussed in
	http:#www.geeksforgeeks.org/next-higher-number-with-same-number-of-set-bits/
	"""
	if (x):
		rightOne = x & (-x)
		nextHigherOneBit = x + rightOne

		rightOnesPattern = x ^ nextHigherOneBit

		rightOnesPattern = (rightOnesPattern) // rightOne

		rightOnesPattern >>= 2

		next = nextHigherOneBit | rightOnesPattern

	return next

# function to find the mth smallest
# number having k number of set bits


def mthSmallestWithKSetBits(m, k):

	# smallest number having 'k'
	# number of set bits
	num = (1 << k) - 1

	# finding the mth smallest number
	# having k set bits
	for i in range(1, m):
		num = nxtHighWithNumOfSetBits(num)

	# required number
	return num


# Driver Code
if __name__ == '__main__':
	m = 6
	k = 4
	print(mthSmallestWithKSetBits(m, k))

# This code is contributed by
# Shubham Singh(SHUBHAMSINGH10)
