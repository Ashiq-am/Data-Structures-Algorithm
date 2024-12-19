# Python3 implementation to find
# the smallest number with n set
# and m unset bits

# function to toggle bits in the
# given range
def toggleBitsFromLToR(n, l, r):

	# for invalid range
	if (r < l):
		return n

	# calculating a number 'num'
	# having 'r' number of bits
	# and bits in the range l
	# to r are the only set bits
	num = ((1 << r) - 1) ^ ((1 << (l - 1)) - 1)

	# toggle bits in the range
	# l to r in 'n' and return the number
	return (n ^ num)

# function to find the smallest number
# with n set and m unset bits
def smallNumWithNSetAndMUnsetBits(n, m):

	# calculating a number 'num' having
	# '(n+m)' bits and all are set
	num = (1 << (n + m)) - 1

	# required smallest number
	return toggleBitsFromLToR(num, n, n + m - 1);


# Driver program to test above
n = 2
m = 2

ans = smallNumWithNSetAndMUnsetBits(n, m)
print (ans)

# This code is contributed by Saloni Gupta
