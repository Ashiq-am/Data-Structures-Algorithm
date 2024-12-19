# Python implementation
# to toggle bits in
# the given range

# function to toggle bits
# in the given range


def toggleBitsFromLToR(n, l, r):

	# calculating a number
	# 'num' having 'r'
	# number of bits and
	# bits in the range l
	# to r are the only set bits
	num = ((1 << r) - 1) ^ ((1 << (l - 1)) - 1)

	# toggle bits in the
	# range l to r in 'n'
	# Besides this, we can calculate num as: num=(1<<r)-l .

	# and return the number
	return (n ^ num)

# Driver code


n = 50
l = 2
r = 5

print(toggleBitsFromLToR(n, l, r))

# This code is contributed
# by Anant Agarwal.
