# Python3 program to check whether number
# has only first and last bits set

# function to check whether 'n'
# is a power of 2 or not
def powerOfTwo (n):
	return (not(n & n-1))


# function to check whether number
# has only first and last bits set
def onlyFirstAndLastAreSet (n):

	if (n == 1):
		return True
	return powerOfTwo (n-1)

# Driver program to test above
n = 9
if (onlyFirstAndLastAreSet (n)):
	print('Yes')
else:
	print('No')

# This code is contributed by Shariq Raza
