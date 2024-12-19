# Recursive function to return gcd of a and b
def gcd(a, b):
	if (a == b):
		return a

	return gcd(a-b, b) if (a > b) else gcd(a, b-a)

# This code is contributed by subham348.
