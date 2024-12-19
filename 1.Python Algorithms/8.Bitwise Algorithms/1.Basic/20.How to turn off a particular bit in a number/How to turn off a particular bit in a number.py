# Returns a number that
# has all bits same as n
# except the k'th bit
# which is made 0

def turnOffK(n,k):

	# k must be greater than 0
	if (k <= 0):
		return n

	# Do & of n with a number
	# with all set bits except
	# the k'th bit
	return (n & ~(1 << (k - 1)))


# Driver code
n = 15
k = 4
print(turnOffK(n, k))

# This code is contributed
# by Anant Agarwal.
