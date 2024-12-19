# Python code for swapping given bits of a number
def swapBits(n, p1, p2):

# left-shift 1 p1 and p2 times
# and using XOR
	if ((n & (1 << p1)) >> p1) ^ ((n & (1 << p2)) >> p2):
		n ^= 1 << p1
		n ^= 1 << p2
	return n

# Driver Code
print("Result =",swapBits(28, 0, 3))

# This code is contributed by rag2127
