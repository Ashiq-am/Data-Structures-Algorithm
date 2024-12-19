# Python3 program to obtain maximum
# XOR value sub-array
import math

# Function to calculate maximum XOR value
def maxXOR(n, k):
	c = int(math.log(n, 2)) + 1

	# Return (2^c - 1)
	return ((1 << c) - 1)

# Driver Code
n = 12; k = 3
print (maxXOR(n, k))

# This code is contributed by shreyanshi_arun.
