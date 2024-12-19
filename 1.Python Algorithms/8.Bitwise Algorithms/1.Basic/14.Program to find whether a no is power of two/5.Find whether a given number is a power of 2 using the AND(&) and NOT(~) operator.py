# Python program of the above approach

# Function to check if x is power of 2*/


def isPowerofTwo(n):

	if (n == 0):
		return 0
	if ((n & (~(n - 1))) == n):
		return 1
	return 0


# Driver code
if __name__ == "__main__":

	# Function call
	if(isPowerofTwo(30)):
		print('Yes')
	else:
		print('No')

	if(isPowerofTwo(128)):
		print('Yes')
	else:
		print('No')

# This code is contributed by shivanisinghss2110
