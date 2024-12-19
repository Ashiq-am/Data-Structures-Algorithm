# Python program to count of ways to place 1 x 4 tiles
# on n x 4 grid.

# Returns count of count of ways to place 1 x 4 tiles
# on n x 4 grid.
def count(n):

	# Create a table to store results of subproblems
	# dp[i] stores count of ways for i x 4 grid.
	dp = [0 for _ in range(n+1)]

	# Fill the table from d[1] to dp[n]
	for i in range(1,n+1):

		# Base cases
		if i <= 3:
			dp[i] = 1
		elif i == 4:
			dp[i] = 2
		else:
			# dp(i-1) : Place first tile horizontally
			# dp(n-4) : Place first tile vertically
			#		 which means 3 more tiles have
			#		 to be placed vertically.
			dp[i] = dp[i-1] + dp[i-4]

	return dp[n]

# Driver code to test above
n = 5
print ("Count of ways is"),
print (count(n))
