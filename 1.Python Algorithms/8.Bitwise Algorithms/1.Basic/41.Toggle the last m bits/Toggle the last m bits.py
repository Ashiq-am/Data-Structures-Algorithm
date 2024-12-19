# Python implementation to
# toggle the last m bits

# function to toggle
# the last m bits
def toggleLastMBits(n,m):

	# calculating a number
	# 'num' having 'm' bits
	# and all are set.
	num = (1 << m) - 1

	# toggle the last m bits
	# and return the number
	return (n ^ num)

# Driver code

n = 107
m = 4
print(toggleLastMBits(n, m))

# This code is contributed
# by Anant Agarwal.
