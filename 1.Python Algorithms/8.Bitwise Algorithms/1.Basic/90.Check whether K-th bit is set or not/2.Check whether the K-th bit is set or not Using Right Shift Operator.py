# PHP program to check if k-th bit of
# a given number is set or not using
# right shift operator.


def isKthBitSet(n, k):
	if ((n >> (k - 1)) and 1):
		print("SET")
	else:
		print("NOT SET")


# Driver code
if __name__ == "__main__":
	n, k = 5, 1

	# Function call
	isKthBitSet(n, k)

# This code contributed by
# PrinciRaj1992
