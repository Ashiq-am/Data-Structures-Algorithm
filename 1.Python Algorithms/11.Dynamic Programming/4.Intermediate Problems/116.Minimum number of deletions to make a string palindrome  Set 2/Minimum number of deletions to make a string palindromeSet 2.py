# Python3 program to find minimum deletions
# to make palindrome.
INT_MAX = 99999999999

def getLevenstein(inpt):

	# Find reverse of input string
	revInput = inpt[::-1]

	# Create a DP table for storing
	# edit distance of string and reverse.
	n = len(inpt)
	dp = [[-1 for _ in range(n + 1)]
			for __ in range(n + 1)]
	for i in range(n + 1):
		dp[0][i] = i
		dp[i][0] = i

	# Find edit distance between
	# input and revInput considering
	# only delete operation.
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			if inpt[i - 1] == revInput[j - 1]:
				dp[i][j] = dp[i - 1][j - 1]
			else:
				dp[i][j] = 1 + min(dp[i - 1][j],
								dp[i][j - 1])

	# Go from bottom left to top right
	# and find the minimum
	res = INT_MAX
	i, j = n, 0
	while i >= 0:
		res = min(res, dp[i][j])
		if i < n:
			res = min(res, dp[i + 1][j])
		if i > 0:
			res = min(res, dp[i - 1][j])
		i -= 1
		j += 1
	return res

# Driver Code
if __name__ == "__main__":
	inpt = "myfirstgeekarticle"
	print(getLevenstein(inpt))
