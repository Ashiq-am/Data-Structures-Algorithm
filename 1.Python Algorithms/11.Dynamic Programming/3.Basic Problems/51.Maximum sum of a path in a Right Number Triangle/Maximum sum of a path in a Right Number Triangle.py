# Python program to print maximum sum
# in a right triangle of numbers.

# tri[][] is a 2D array that stores the
# triangle, n is number of lines or rows.
def maxSum(tri, n):

	# Adding the element of row 1 to both the
	# elements of row 2 to reduce a step from
	# the loop
	if n > 1:
		tri[1][1] = tri[1][1]+tri[0][0]
		tri[1][0] = tri[1][0]+tri[0][0]

	# Traverse remaining rows
	for i in range(2, n):
		tri[i][0] = tri[i][0] + tri[i-1][0]
		tri[i][i] = tri[i][i] + tri[i-1][i-1]

		# Loop to traverse columns
		for j in range(1, i):

			# Checking the two conditions, directly below
			# and below right. Considering the greater one

			# tri[i] would store the possible combinations
			# of sum of the paths
			if tri[i][j]+tri[i-1][j-1] >= tri[i][j]+tri[i-1][j]:
				tri[i][j] = tri[i][j] + tri[i-1][j-1]
			else:
				tri[i][j] = tri[i][j]+tri[i-1][j]

	# array at n-1 index (tri[i]) stores all possible
	# adding combination, finding the maximum one
	# out of them
	print(max(tri[n-1]))

# driver program
tri = [[1], [2,1], [3,3,2]]
maxSum(tri, 3)
