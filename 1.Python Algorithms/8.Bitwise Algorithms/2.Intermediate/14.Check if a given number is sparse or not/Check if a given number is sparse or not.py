# Python program to check
# if n is sparse or not

# Return true if n is
# sparse, else false


def checkSparse(n):

	# n is not sparse if there is set
	# in AND of n and n/2
	if (n & (n >> 1)):
		return 0

	return 1


# Driver code
if __name__ == "__main__":

	# Function call
	print(checkSparse(72))
	print(checkSparse(12))
	print(checkSparse(2))
	print(checkSparse(30))

# This code is contributed
# by Anant Agarwal.
