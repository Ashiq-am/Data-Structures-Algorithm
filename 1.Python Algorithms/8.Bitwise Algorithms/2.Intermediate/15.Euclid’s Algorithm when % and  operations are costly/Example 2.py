# Python3 Function to return gcd of a and b
def gcd(a, b):

	if (a == 0):
		return b

	return gcd(b % a, a)

# This code is contributed by phasing17
