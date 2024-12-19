# Python3 code to check if k-th bit
# of a given number is set or not


def isKthBitSet(n, k):
	if n & (1 << (k - 1)):
		print("SET")
	else:
		print("NOT SET")


# Driver code
if __name__ == "__main__":
	n = 5
	k = 1

	# Function call
	isKthBitSet(n, k)

# This code is contributed by "Sharad_Bhardwaj".
