# Python program to swap three variables
# without using temporary variable

# Assign c's value to a, a's value to b and
# b's value to c.
def swapThree(a, b, c) :

	# Store XOR of all in a
	a[0] = a[0] ^ b[0] ^ c[0]

	# After this, b has value of a[0]
	b[0] = a[0] ^ b[0] ^ c[0]

	# After this, c has value of b
	c[0] = a[0] ^ b[0] ^ c[0]

	# After this, a[0] has value of c
	a[0] = a[0] ^ b[0] ^ c[0]

# Driver code
a, b, c = [10], [20], [30]

print("Before swapping a = ", a[0],
	", b = ", b[0], ", c = ", c[0])

swapThree(a, b, c)

print("After swapping a = ", a[0],
", b = ", b[0], ", c = ", c[0])

# This code is contributed by SHUBHAMSINGH10
