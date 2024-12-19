# Python Program to
# subtract two Number
# without using arithmetic operator
# Recursive implementation.

def subtract(x, y):

	if (y == 0):
		return x
	return subtract(x ^ y, (~x & y) << 1)

# Driver program
x = 29
y = 13
print("x - y is", subtract(x, y))

# This code is contributed by
# Smitha Dinesh Semwal
