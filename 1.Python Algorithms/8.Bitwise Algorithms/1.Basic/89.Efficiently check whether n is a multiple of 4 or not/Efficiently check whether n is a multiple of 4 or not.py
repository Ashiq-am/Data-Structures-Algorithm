# Python 3 implementation to
# efficiently check whether n
# is a multiple of 4 or not

# function to check whether 'n'
# is a multiple of 4 or not
def isAMultipleOf4(n):

	# if true, then 'n' is
	# a multiple of 4
	if ((n & 3) == 0):
		return "Yes"

	# else 'n' is not a
	# multiple of 4
	return "No"

# Driver Code
if __name__ == "__main__":

	n = 16
	print (isAMultipleOf4(n))

# This code is contributed
# by ChitraNayal
