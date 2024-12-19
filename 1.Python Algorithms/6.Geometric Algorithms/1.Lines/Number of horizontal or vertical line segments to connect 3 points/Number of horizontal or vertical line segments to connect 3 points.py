# Python program to find number
# of horizontal (or vertical
# line segments needed to
# connect three points.

import math

# Function to check if the
# third point forms a
# rectangle with other
# two points at corners
def isBetween(a, b, c) :

	return min(a, b) <= c and c <= max(a, b)


# Returns true if point k
# can be used as a joining
# point to connect using
# two line segments
def canJoin( x, y, i, j, k) :

	# Check for the valid polyline
	# with two segments
	return (x[k] == x[i] or x[k] == x[j]) and isBetween(y[i], y[j], y[k]) or (y[k] == y[i] or y[k] == y[j]) and isBetween(x[i], x[j], x[k])


def countLineSegments( x, y):

	# Check whether the X-coordinates or
	# Y-cocordinates are same.
	if ((x[0] == x[1] and x[1] == x[2]) or
		(y[0] == y[1] and y[1] == y[2])):
		return 1

	# Iterate over all pairs to check for two
	# line segments
	elif (canJoin(x, y, 0, 1, 2) or
			canJoin(x, y, 0, 2, 1) or
			canJoin(x, y, 1, 2, 0)):
		return 2

	# Otherwise answer is three.
	else:
		return 3
#driver code
x= [-1,-1, 4]
y= [-1, 3, 3]

print(countLineSegments(x, y))
