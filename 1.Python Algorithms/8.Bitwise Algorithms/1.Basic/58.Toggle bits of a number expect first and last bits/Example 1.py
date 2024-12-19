# Python3 program for toggle bits
# expect first and last bit

# return set middle bits
def setmiddlebits(n):

	# set all bit
	n |= n >> 1;
	n |= n >> 2;
	n |= n >> 4;
	n |= n >> 8;
	n |= n >> 16;

	# return middle set bits
	# shift by 1 and xor with 1
	return (n >> 1) ^ 1

def togglemiddlebits(n):

	# if number is 1 then simply return
	if (n == 1):
		return 1

	# xor with middle bits
	return n ^ setmiddlebits(n)

# Driver code
n = 9
print(togglemiddlebits(n))

# This code is contributed by Anant Agarwal.
