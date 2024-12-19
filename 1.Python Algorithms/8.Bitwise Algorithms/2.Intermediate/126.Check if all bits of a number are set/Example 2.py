# Python implementation to
# check whether every
# digit in the binary
# representation of the
# given number is set or not

# function to check if
# all the bits are set
# or not in the binary
# representation of 'n'
def areAllBitsSet(n):

	# all bits are not set
	if (n == 0):
		return "No"

	# if true, then all bits are set
	if (((n + 1) & n) == 0):
		return "Yes"

	# else all bits are not set
	return "No"


# Driver program to test above

n = 7
print(areAllBitsSet(n))

# This code is contributed
# by Anant Agarwal.
