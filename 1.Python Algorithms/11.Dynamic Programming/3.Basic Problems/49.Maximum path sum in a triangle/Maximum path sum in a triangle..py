# Python program for
# Dynamic Programming
# implementation of Max
# sum problem in a
# triangle

N = 3

# Function for finding maximum sum
def maxPathSum(tri, m, n):

	# loop for bottom-up calculation
	for i in range(m-1, -1, -1):
		for j in range(i+1):

			# for each element, check both
			# elements just below the number
			# and below right to the number
			# add the maximum of them to it
			if (tri[i+1][j] > tri[i+1][j+1]):
				tri[i][j] += tri[i+1][j]
			else:
				tri[i][j] += tri[i+1][j+1]

	# return the top element
	# which stores the maximum sum
	return tri[0][0]

# Driver program to test above function

tri = [[1, 0, 0],
	[4, 8, 0],
	[1, 5, 3]]
print(maxPathSum(tri, 2, 2))
