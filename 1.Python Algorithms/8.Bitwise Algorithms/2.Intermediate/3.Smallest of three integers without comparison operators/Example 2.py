# Python3 implementation of above approach
CHAR_BIT = 8

# Function to find minimum of x and y
def min(x, y):
	return y + ((x - y) & ((x - y) >> (32 * CHAR_BIT - 1)))

# Function to find minimum
# of 3 numbers x, y and z
def smallest(x, y, z):
	return min(x, min(y, z))

# Driver code
x = 12
y = 15
z = 5
print("Minimum of 3 numbers is ",
			smallest(x, y, z))

# This code is contributed
# by Mohit Kumar
