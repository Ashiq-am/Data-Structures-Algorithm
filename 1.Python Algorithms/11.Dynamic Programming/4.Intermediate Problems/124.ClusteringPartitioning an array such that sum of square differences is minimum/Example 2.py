# Python3 program to find minimum cost k partitions
# of array.
inf = 1000000000

# Returns minimum cost of partitioning a[] in
# k clusters.
def minCost(a, n, k):

	# Create a dp[][] table and initialize
	# all values as infinite. dp[i][j] is
	# going to store optimal partition cost
	# for arr[0..i-1] and j partitions
	dp = [[inf for i in range(k + 1)]
			for j in range(n + 1)]

	# Fill dp[][] in bottom up manner
	dp[0][0] = 0

	# Current ending position (After i-th
	# iteration result for a[0..i-1] is computed.
	for i in range(1, n + 1):

		# j is number of partitions
		for j in range(1, k + 1):

			# Picking previous partition for
			# current i.
			for m in range(i - 1, -1, -1):
				dp[i][j] = min(dp[i][j], dp[m][j - 1] +
									(a[i - 1] - a[m]) *
									(a[i - 1] - a[m]))

	return dp[n][k]

# Driver code
if __name__ == '__main__':
	k = 2
	a = [1, 5, 8, 10]
	n = len(a)
	print(minCost(a, n, k))


