# Python3 program to find
# Maximum path sum
# start any column in
# row '0' and ends
# up to any column in row 'n-1'

N = 4

# function find maximum sum path
def MaximumPath(Mat):

	result = 0

	# create 2D matrix to store the sum
	# of the path
	# initialize all dp matrix as '0'
	dp = [[0 for i in range(N+2)] for j in range(N)]

	# copy all element of first column into
	# dp first column
	for i in range(N):
		for j in range(1, N+1):
			dp[i][j] = max(dp[i-1][j-1],
						max(dp[i-1][j],
							dp[i-1][j+1])) + \
					Mat[i][j-1]

	# Find maximum path sum that end ups
	# at any column of last row 'N-1'
	for i in range(N+1):
		result = max(result, dp[N-1][i])

	# return maximum sum path
	return result

# driver program to test above function
Mat = [[4, 2, 3, 4],
	[2, 9, 1, 10],
	[15, 1, 3, 0],
	[16, 92, 41, 44]]

print(MaximumPath(Mat))
