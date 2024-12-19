# Python3 program to find XNOR of two numbers.
import math

# Returns XNOR of num1 and num2
def XNOR(a, b):

	# getting the number of bits from
	# max of a and b to construct the bit mask
	numOfBits = int(math.log(max(a, b), 2))

	# constructing the bit mask
	mask = (1 << numOfBits) - 1

	# xnor = inverted xor
	xnor = ~(a ^ b)

	# getting only the required bits
	# using the mask
	return xnor & mask


# Driver code
num1 = 7
num2 = 19

# function call
print(XNOR(num1, num2))

# This code is contributed by phasing17
