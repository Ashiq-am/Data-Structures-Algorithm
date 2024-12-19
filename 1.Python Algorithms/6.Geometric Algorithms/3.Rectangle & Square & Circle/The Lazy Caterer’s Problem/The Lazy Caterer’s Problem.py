# A Python 3 program to
# find the solution to
# The Lazy Caterer's Problem

# This function receives an
# integer n and returns the
# maximum number of pieces
# that can be made form
# pancake using n cuts
def findPieces( n ):

	# Use the formula
	return (n * ( n + 1)) // 2 + 1

# Driver Code
print(findPieces(1))
print(findPieces(2))
print(findPieces(3))
print(findPieces(50))

# This code is contributed
# by ihritik
