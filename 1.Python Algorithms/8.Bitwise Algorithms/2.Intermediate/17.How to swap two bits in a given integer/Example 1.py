# Python3 program for the above approach

# This function swaps bit at positions p1 and p2 in an integer n
def swapBits(n, p1, p2):

	# Move p1'th to rightmost side
	bit1 = (n >> p1) & 1

	# Move p2'th to rightmost side
	bit2 = (n >> p2) & 1

	# XOR the two bits
	x = (bit1 ^ bit2)

	# Put the xor bit back to their original positions
	x = (x << p1) | (x << p2)

	# XOR 'x' with the original number so that the
	# two sets are swapped
	result = n ^ x
	return result


# Driver program to test above function
if __name__ == '__main__':
	res = swapBits(28, 0, 3)
	print("Result = ", res)

# This code is contributed by nirajgusain5
