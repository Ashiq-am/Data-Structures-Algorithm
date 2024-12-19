# Python implementation to
# find the largest number
# with n set and m unset bits

# function to toggle
# the last m bits
def toggleLastMBits(n,m):

	# if no bits are required
	# to be toggled
	if (m == 0):
		return n

	# calculating a number
	# 'num' having 'm' bits
	# and all are set
	num = (1 << m) - 1

	# toggle the last m bits
	# and return the number
	return (n ^ num)


# function to find
# the largest number
# with n set and m unset bits
def largeNumWithNSetAndMUnsetBits(n,m):

	# calculating a number
	# 'num' having '(n+m)' bits
	# and all are set
	num = (1 << (n + m)) - 1

	# required largest number
	return toggleLastMBits(num, m)

# Driver code

n = 2
m = 2

print(largeNumWithNSetAndMUnsetBits(n, m))

# This code is contributed
# by Anant Agarwal.
