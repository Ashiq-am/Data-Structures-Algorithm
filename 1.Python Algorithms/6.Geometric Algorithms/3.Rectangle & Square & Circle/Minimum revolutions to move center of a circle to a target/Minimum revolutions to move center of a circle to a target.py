# Python program to find
# minimum number of
# revolutions to reach
# a target center
import math

# Minimum revolutions to move center from
# (x1, y1) to (x2, y2)
def minRevolutions(r,x1,y1,x2,y2):

	d = math.sqrt((x1 -x2)*(x1 - x2) +
		(y1 - y2)*(y1 - y2))
	return math.ceil(d//(2*r))

# Driver code

r = 2
x1 = 0
y1 = 0
x2 = 0
y2 = 4

print(minRevolutions(r, x1, y1, x2, y2))

# This code is contributed
# by Anant Agarwal.
