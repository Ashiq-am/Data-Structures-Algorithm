# Bitwise operator based
# function to check divisibility by 9

def isDivBy9(n):

	# Base cases
	if (n == 0 or n == 9):
		return True
	if (n < 9):
		return False

	# If n is greater than 9,
	# then recur for [floor(n / 9) - n % 8]
	return isDivBy9((int)(n>>3) - (int)(n&7))

# Driver code

# Let us print all multiples
# of 9 from 0 to 100
# using above method
for i in range(100):
	if (isDivBy9(i)):
		print(i, " ", end ="")

# This code is contributed
# by Anant Agarwal.
