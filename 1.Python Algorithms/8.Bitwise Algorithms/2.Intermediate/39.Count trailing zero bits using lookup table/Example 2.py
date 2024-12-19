# Python3 code for counting trailing zeros
# in binary representation of a number

def countTrailingZero(x):

	# Map a bit value mod 37 to its position
	lookup = [32, 0, 1, 26, 2, 23, 27, 0,
			3, 16, 24, 30, 28, 11, 0, 13,
			4, 7, 17, 0, 25, 22, 31, 15,
			29, 10, 12, 6, 0, 21, 14, 9,
			5, 20, 8, 19, 18]

	# Only difference between (x and -x) is
	# the value of signed magnitude(leftmostbit)
	# negative numbers signed bit is 1
	return lookup[(-x & x) % 37]

# Driver Code
if __name__ == "__main__":

	print(countTrailingZero(48))

# This code is contributed
# by Rituraj Jain
