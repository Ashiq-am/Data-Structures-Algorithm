# Program to print 1 with 75% probability and 0
# with 25% probability
from random import randrange

# Random Function to that returns 0 or 1 with
# equal probability
def rand50():
		# rand range function generates a integer between
	# the provided ranges which is half closed interval
	# It will generate integer 0 or 1 if passed 0,2 as parameter
	return (int)(randrange(0, 2)) & 1

# Random Function to that returns 1 with 75%
# probability and 0 with 25% probability using
# left shift and Bitwise XOR


def rand75():

	# x is one of {0, 1}
	x = rand50()
	x = x << 1

	# x is now one of {00, 10}
	x = x ^ rand50()

	# x is now one of {00, 01, 10, 11}
	return 1 if (x > 0) else 0

# Driver code to test above functions
for i in range(0, 50):
	print(rand75(), end="")

	# This code is contributed by meetgor.
