# Python3 program to find count of
# values whose XOR with x is equal
# to the sum of value and x and
# values are smaller than equal to x


def FindValues(x):

	# Initialize result
	count = 0

	# Traversing through all values
	# between 0 and x both inclusive
	# and counting numbers that
	# satisfy given property
	for i in range(0, x):
		if ((x + i) == (x ^ i)):
			count = count + 1

	return count


# Driver code
x = 10

# Function call
print(FindValues(x))

# This code is contributed
# by Shivi_Aggarwal
