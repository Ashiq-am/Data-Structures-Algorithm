# Python3 program to find the probability of
# the Knight to remain inside the chessboard
# after taking exactly K number of steps
# size of the chessboard
N = 8

# Direction vector for the Knight
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

# returns true if the knight
# is inside the chessboard

def inside(x, y):
	return (x >= 0 and x < N and y >= 0 and y < N)

# Bottom up approach for finding the
# probability to go out of chessboard.

def findProb(start_x, start_y, steps):

	# dp array
	dp1 = [[[0 for i in range(N+5)]
			for j in range(N+5)]
			for k in range(steps + 5)]

	# For 0 number of steps, each
	# position will have probability 1
	for i in range(N):
		for j in range(N):
			dp1[i][j][0] = 1

	# for every number of steps s
	for s in range(1, steps + 1):

		# for every position (x,y) after
		# s number of steps
		for x in range(N):

			for y in range(N):
				prob = 0.0

				# For every position reachable from (x,y)
				for i in range(8):
					nx = x + dx[i]
					ny = y + dy[i]

					# if this position lie inside the board
					if (inside(nx, ny)):
						prob += dp1[nx][ny][s-1] / 8.0

				# store the result
				dp1[x][y][s] = prob

	# return the result
	return dp1[start_x][start_y][steps]

# Driver code

# number of steps
K = 3

# Function Call
print(findProb(0, 0, K))

# This code is contributed by Anant Agarwal.
