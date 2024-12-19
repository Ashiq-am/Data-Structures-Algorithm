# Python3 implementation to
# set the rightmost unset bit
import math


def setRightmostUnsetBit(n):

	# if all bits of 'n' are set
	# the number is of form 2^k -1 return n
	if ((n & (n + 1)) == 0):
		return n
	# else
	return n | (n+1)

# Driver code


n = 21
print(setRightmostUnsetBit(n))

# This code is contributed by Kasina Dheeraj.
