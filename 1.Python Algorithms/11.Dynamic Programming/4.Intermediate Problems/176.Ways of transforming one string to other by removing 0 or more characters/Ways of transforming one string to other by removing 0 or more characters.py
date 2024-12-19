# Python3 program to count the distinct
# transformation of one string to other.

def countTransformation(a, b):
	n = len(a)
	m = len(b)

	# If b = "" i.e., an empty string. There
	# is only one way to transform (remove all
	# characters)
	if m == 0:
		return 1

	dp = [[0] * (n) for _ in range(m)]

	# Fill dp[][] in bottom up manner
	# Traverse all character of b[]
	for i in range(m):

		# Traverse all characters of a[] for b[i]
		for j in range(i, n):

			# Filling the first row of the dp
			# matrix.
			if i == 0:
				if j == 0:
					if a[j] == b[i]:
						dp[i][j] = 1
					else:
						dp[i][j] = 0
				elif a[j] == b[i]:
					dp[i][j] = dp[i][j - 1] + 1
				else:
					dp[i][j] = dp[i][j - 1]

			# Filling other rows
			else:
				if a[j] == b[i]:
					dp[i][j] = (dp[i][j - 1] +
								dp[i - 1][j - 1])
				else:
					dp[i][j] = dp[i][j - 1]
	return dp[m - 1][n - 1]

# Driver Code
if __name__ == "__main__":
	a = "abcccdf"
	b = "abccdf"
	print(countTransformation(a, b))
