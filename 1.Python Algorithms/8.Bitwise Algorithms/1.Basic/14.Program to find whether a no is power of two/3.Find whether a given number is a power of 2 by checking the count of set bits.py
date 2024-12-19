# Python3 program to check if given
# number is power of 2 or not

# Function to check if x is power of 2


def isPowerOfTwo(n):
	cnt = 0
	while n > 0:
		if n & 1 == 1:
			cnt = cnt + 1
		n = n >> 1

	if cnt == 1:
		return 1
	return 0


# Driver code
if __name__ == "__main__":

	# Function call
	if(isPowerOfTwo(31)):
		print('Yes')
	else:
		print('No')

	if(isPowerOfTwo(64)):
		print('Yes')
	else:
		print('No')

# This code is contributed by devendra salunke
