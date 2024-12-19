# Simple Python3 program to set all even
# bits of a number
from math import log

# function to set all the even bits
def setEvenBits(n):

	# calculating number of bits using log
	numOfBits = 1 + int(log(n, 2))

	# if there is only one bit,
	if numOfBits == 1:
		return n

	# calculating the max power of GP series
	m = int((numOfBits - 1 ^ (numOfBits % 1)) / 2)

	# calculating mask using GP sum
	# which is a(r ^ n - 1) / (r - 1)
	# where a = 2, r = 4, n = m
	mask = int((2 * ((1 << (2 * m)) - 1)) / 3)

	# toggling all even bits using mask | n
	return mask | n

# Driver Code
n = 102121
print(setEvenBits(n))

# This code is contributed by phasing17
