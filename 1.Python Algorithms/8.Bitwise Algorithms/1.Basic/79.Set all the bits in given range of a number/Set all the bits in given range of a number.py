# Python3 implementation to Set
# bits in the given range

# Function to toggle bits
# in the given range
def setallbitgivenrange(n, l, r):

	# calculating a number 'range'
	# having set bits in the range
	# from l to r and all other
	# bits as 0 (or unset).
	range = (((1 << (l - 1)) - 1) ^ ((1 << (r)) - 1))

	return (n | range)

# Driver code
n, l, r = 17, 2, 3
print(setallbitgivenrange(n, l, r))

# This code is contributed by Anant Agarwal.
