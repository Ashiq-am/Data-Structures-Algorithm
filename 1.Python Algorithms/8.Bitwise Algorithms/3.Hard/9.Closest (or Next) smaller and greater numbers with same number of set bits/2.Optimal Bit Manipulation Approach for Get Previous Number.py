# Python3 Implementation of getPrev in
# Same number of bits 1's is below

# Main Function to find next Bigger number
# Smaller than n


def getPrev(n):

	# Compute c0 and c1 and store N
	temp = n
	c0 = 0
	c1 = 0

	while ((temp & 1) == 1):
		c1 = c1+1
		temp = temp >> 1

	if (temp == 0):
		return -1

	while (((temp & 1) == 0) and (temp != 0)):
		c0 = c0+1
		temp = temp >> 1

	# position of rightmost non-trailing one.
	p = c0 + c1

	# clears from bit p onwards
	n = n & ((~0) << (p + 1))

	# Sequence of (c1+1) ones
	mask = (1 << (c1 + 1)) - 1

	n = n | mask << (c0 - 1)

	return n


if __name__ == '__main__':
	n = 6 # input 1
	print(getPrev(n))

	n = 16	 # input 2
	print(getPrev(n))

# This code is contributed by nirajgusain5
