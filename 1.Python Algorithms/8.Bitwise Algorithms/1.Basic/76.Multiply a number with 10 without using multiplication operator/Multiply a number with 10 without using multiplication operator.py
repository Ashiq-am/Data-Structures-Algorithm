# Python 3 program to multiply a
# number with 10 using bitwise
# operators

# Function to find multiplication
# of n with 10 without using
# multiplication operator
def multiplyTen(n):

	return (n << 1) + (n << 3)

# Driver program to run the case
n = 50
print (multiplyTen(n))

# This code is contributed by
# Smitha
