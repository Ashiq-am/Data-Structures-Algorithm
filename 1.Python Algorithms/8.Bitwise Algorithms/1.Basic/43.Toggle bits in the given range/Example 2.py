# Python3 implementation to toggle bits in
# the given range

# Function to toggle bits in the given range
def toggleBitsFromLToR(N, L, R):

	res = N
	for i in range(L, R + 1):

		# Set bit
		if ((N & (1 << (i - 1))) != 0):

			# XOR will set 0 to already set
			# bits(a^a=0)
			res = res ^ (1 << (i - 1))

		# unset bits
		else:
			# OR will set'0'bits to 1
			res = res | (1 << (i - 1))

	return res

# Driver code
n = 50
l = 2
r = 5
print(toggleBitsFromLToR(n, l, r))

# This code is contributed by phasing17
