# An optimized Python program to count
# unset bits in an integer.
import math

def countUnsetBits(n):
	x = n

	# Make all bits set MSB(including MSB)

	# This makes sure two bits(From MSB
	# and including MSB) are set
	n |= n >> 1

	# This makes sure 4 bits(From MSB and
	# including MSB) are set
	n |= n >> 2

	n |= n >> 4
	n |= n >> 8
	n |= n >> 16

	t = math.log(x ^ n, 2)

	# Count set bits in toggled number
	return math.floor(t)

# Driver code
n = 17
print(countUnsetBits(n))

# This code is contributed 29AjayKumar
