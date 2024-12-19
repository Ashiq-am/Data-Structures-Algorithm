# Python3 program for
# finding maximum squares
# that can fit in
# right angle isosceles
# triangle

# function for finding max squares
def maxSquare(b, m):

	# return in O(1) with derived
	# formula
	return (b / m - 1) * (b / m) / 2


# driver program
b = 10
m = 2
print(int(maxSquare (b,m)))

# This code is contributed by
# Smitha Dinesh Semwal
