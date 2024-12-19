# Python program to change even
# bits to 0.

# Returns modified number with
# all even bits 0.


def changeEvenBits(n):

	# To store sum of bits
	# at even positions.
	to_subtract = 0

	# To store bits to shift
	m = 0

	# One by one put all even
	# bits to end
	x = n
	while(x):

		# If current last bit
		# is set, add it to ans
		if (x & 1):
			to_subtract += (1 << m)

		# Next shift position
		m += 2
		x >>= 2

	return n - to_subtract


# Driver code
n = 30
print(changeEvenBits(n))

# This code is contributed by Sachin Bisht
