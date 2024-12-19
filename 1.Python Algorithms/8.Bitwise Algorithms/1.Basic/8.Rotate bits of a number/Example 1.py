# Python3 code to
# rotate bits of number

INT_BITS = 32

# Function to left
# rotate n by d bits
def leftRotate(n, d):

	# In n<<d, last d bits are 0.
	# To put first 3 bits of n at
	# last, do bitwise or of n<<d
	# with n >>(INT_BITS - d)
	return (n << d)|(n >> (INT_BITS - d))

# Function to right
# rotate n by d bits
def rightRotate(n, d):

	# In n>>d, first d bits are 0.
	# To put last 3 bits of at
	# first, do bitwise or of n>>d
	# with n <<(INT_BITS - d)
	return (n >> d)|(n << (INT_BITS - d)) & 0xFFFFFFFF

# Driver program to
# test above functions
n = 16
d = 2

print("Left Rotation of",n,"by"
	,d,"is",end=" ")
print(leftRotate(n, d))

print("Right Rotation of",n,"by"
	,d,"is",end=" ")
print(rightRotate(n, d))

# This code is contributed by
# Smitha Dinesh Semwal
