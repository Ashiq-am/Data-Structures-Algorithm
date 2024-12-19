# Python3 implementation to find the
# position of rightmost same bit
import math

# Function to find the position
# of rightmost set bit in 'n'
def getRightMostSetBit(n):

	return int(math.log2(n & -n)) + 1

# Function to find the position of
# rightmost same bit in the binary
# representations of 'm' and 'n'
def posOfRightMostSameBit(m, n):

	# position of rightmost same bit
	return getRightMostSetBit(~(m ^ n))

# Driver Code
m, n = 16, 7
print("Position = ", posOfRightMostSameBit(m, n))

# This code is contributed by Anant Agarwal.
