# Python program for above implementation

# Function to set the bits
def setBits(n, m, i, j):

	# number with all 1's
	allOnes = not 0

	# Set all the bits in the left of j
	left = allOnes << (j + 1)

	# Set all the bits in the right of j
	right = ((1 << i) - 1)

	# Do Bitwise OR to get all the bits
	# set except in the range from i to j
	mask = left | right

	# clear bits j through i
	masked_n = n & mask

	# move m into the correct position
	m_shifted = m << i

	# return the Bitwise OR of masked_n
	# and shifted_m
	return (masked_n | m_shifted)

# Drivers program
n, m = 2, 4
i, j = 2, 4
print(setBits(n, m, i, j))

# This code is submitted by Sachin Bisht
