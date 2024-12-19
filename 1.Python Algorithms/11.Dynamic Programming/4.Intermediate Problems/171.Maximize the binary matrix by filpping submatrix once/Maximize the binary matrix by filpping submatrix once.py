# Python 3 program to find maximum number of
# ones after one flipping in Binary Matrix
R = 3
C = 3

# Return number of ones in square submatrix
# of size k x k starting from (x, y)
def cal(ones, x, y, k):
	return (ones[x + k - 1][y + k - 1] -
			ones[x - 1][y + k - 1] -
			ones[x + k - 1][y - 1] +
			ones[x - 1][y - 1])

# Return maximum number of 1s after
# flipping a submatrix
def sol(mat):
	ans = 0

	# Precomputing the number of 1s
	ones = [[0 for i in range(C + 1)]
			for i in range(R + 1)]
	for i in range(1, R + 1, 1):
		for j in range(1, C + 1, 1):
			ones[i][j] = (ones[i - 1][j] + ones[i][j - 1] -
						ones[i - 1][j - 1] +
						(mat[i - 1][j - 1] == 1))

	# Finding the maximum number of 1s
	# after flipping
	for k in range(1, min(R, C) + 1, 1):
		for i in range(1, R - k + 2, 1):
			for j in range(1, C - k + 2, 1):
				ans = max(ans, (ones[R][C] + k * k - 2 *
							cal(ones, i, j, k)))
	return ans

# Driver code
if __name__ == '__main__':
	mat = [[0, 0, 1],
		[0, 0, 1],
		[1, 0, 1]]

	print(sol(mat))
