SHORT_SIZE = 16

# function to rotate the given unsigned short
# in the left direction
def leftRotate(x, d):

	return (x << d) | (x >> (SHORT_SIZE - d))

# function to rotate the given unsigned short
# in the right direction
def rightRotate(x, d):

	return (x >> d) | (x << (SHORT_SIZE - d)) & 0xDDDDDF

# Driver program to test above functions
# Test case
n = 28
d = 2

print("Left Rotation of",n,"by"
	,d,"is",end=" ")
print(leftRotate(n, d))

print("Right Rotation of",n,"by"
	,d,"is",end=" ")
print(rightRotate(n, d))

# This code is contributed by shivanisinghss2110
