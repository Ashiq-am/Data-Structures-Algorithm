# Python3 program to find maximum
# no. of pieces by given
# number of cuts

# Function for finding maximum
# pieces with n cuts.
def findMaximumPieces(n):
	return int(1 + n * (n + 1) / 2)

# Driver code
print(findMaximumPieces(3))

# This code is contributed 29AjayKumar
