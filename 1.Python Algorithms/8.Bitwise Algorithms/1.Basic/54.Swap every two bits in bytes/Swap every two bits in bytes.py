# Python program to swap every
# two bits in a byte.

import math

def swapBitsInPair( x):

	# Extracting the high bit shift it to lowbit
	# Extracting the low bit shift it to highbit
	return ((x & 0xAAAAAAAA) >> 1) or ((x & 0x55555555) << 1)

# driver Function
x = 4;
print(swapBitsInPair(x))

# This code is contributed by Gitanjali.
