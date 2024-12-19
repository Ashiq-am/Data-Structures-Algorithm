# Python3 program to find
# the first rightmost set
# bit using XOR operator

# function to find the
# rightmost set bit


def PositionRightmostSetbit(n):

	# Position variable initialize
	# with 1 m variable is used
	# to check the set bit
	position = 1
	m = 1

	while (not(n & m)):

		# left shift
		m = m << 1
		position += 1

	return position


# Driver Code
n = 18

# function call
print(PositionRightmostSetbit(n))

# This code is contributed
# by Smitha
