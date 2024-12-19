# Python3 implementation to find the
# position of rightmost different
# bit in two number.
from math import floor, log10

# Function to find rightmost different
# bit in two numbers.


def posOfRightMostDiffBit(m, n):

	return floor(log10(pow(m ^ n, 2))) + 2


# Driver code
if __name__ == '__main__':

	m, n = 52, 4

	# Function call
	print("Position = ",
		posOfRightMostDiffBit(m, n))

# This code is contributed by mohit kumar 29
