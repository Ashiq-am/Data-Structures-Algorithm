# Python implementation
# to find the position
# of rightmost different bit

import math

# Function to find the position of
# rightmost set bit in 'n'


def getRightMostSetBit(n):
	if (n == 0):
		return 0

	return math.log2(n & -n) + 1


# Function to find the position of
# rightmost different bit in the
# binary representations of 'm' and 'n'
def posOfRightMostDiffBit(m, n):

	# position of rightmost different
	# bit
	return getRightMostSetBit(m ^ n)


# Driver code
if __name__ == "__main__":
	m = 52
	n = 4

	# Function call
	print("position = ", int(posOfRightMostDiffBit(m, n)))

# This code is contributed
# by Anant Agarwal.
