# An interesting XOR based
# method to check if a
# number is multiple of 4.

# Returns true if n is a
# multiple of 4.
def isMultipleOf4(n):

	if (n == 1):
		return False

	# Find XOR of all numbers
	# from 1 to n
	XOR = 0
	for i in range(1, n + 1):
		XOR = XOR ^ i

	# If XOR is equal n, then
	# return true
	return (XOR == n)

# Driver code to print
# multiples of 4 Printing
# multiples of 4 using
# above method
for n in range(0, 43):
	if (isMultipleOf4(n)):
		print(n, end = " ")

# This code is contributed
# by Smitha
