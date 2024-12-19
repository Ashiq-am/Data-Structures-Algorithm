# Finds next power of two
# for n. If n itself is a
# power of two then returns n
def nextPowerOf2(n):

	n -= 1
	n |= n >> 1
	n |= n >> 2
	n |= n >> 4
	n |= n >> 8
	n |= n >> 16
	n += 1
	return n

# Driver program to test
# above function
n = 5
print(nextPowerOf2(n))

# This code is contributed
# by Smitha
