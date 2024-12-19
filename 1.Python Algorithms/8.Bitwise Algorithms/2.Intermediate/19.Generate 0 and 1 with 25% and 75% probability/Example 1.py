# Program to print 1 with 75% probability and 0
# with 25% probability
from random import randrange

# Random Function to that returns 0 or 1 with
# equal probability
def rand50():

		# The randrange function will generate integer
	# between the half closed interval at end
	# Here by passing parameter as 0,2
	# the function will generate integer between 0 and 1
	return (int)(randrange(0, 2)) & 1

# Random Function to that returns 1 with 75%
# probability and 0 with 25% probability using
# Bitwise OR
def rand75():
	return rand50() | rand50()

# Driver code to test above functions
for i in range(0, 50):
	print(rand75(), end="")

	# This code is contributed by meetgor.
