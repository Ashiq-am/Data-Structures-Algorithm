# Recursive Python3 program to find minimum jumps
# to reach last building from first.
R = 4
C = 3

def isSafe(x, y):
	return (x < R and y < C)

# Returns minimum jump path from
# (0, 0) to (m, n) in height[R][C]
def minJump(height, x, y):

	# base case
	if (x == R - 1 and y == C - 1):
		return 0

	# Find minimum jumps if we go
	# through diagonal
	diag = 10**9
	if (isSafe(x + 1, y + 1)):
		diag = (minJump(height, x + 1, y + 1) +
					abs(height[x][y] -
						height[x + 1][y + 1]))

	# Find minimum jumps if we go through down
	down = 10**9
	if (isSafe(x + 1, y)):
		down = (minJump(height, x + 1, y) +
					abs(height[x][y] -
						height[x + 1][y]))

	# Find minimum jumps if we go through right
	right = 10**9
	if (isSafe(x, y + 1)):
		right = (minJump(height, x, y + 1) +
					abs(height[x][y] -
						height[x][y + 1]))

	# return minimum jumps
	return min([down, right, diag])

# Driver Code
height = [ [ 5, 4, 2 ],
		[ 9, 2, 1 ],
		[ 2, 5, 9 ],
		[ 1, 3, 11 ] ]

print(minJump(height, 0, 0))

