# Python3 program to calculate Minimum cost
# to make Longest Common Subsequence of length k
N = 30

# Return Minimum cost to make LCS of length k
def solve(X, Y, l, r, k, dp):

	# If k is 0
	if k == 0:
		return 0

	# If length become less than 0,
	# return big number
	if l < 0 or r < 0:
		return 1000000000

	# If state already calculated
	if dp[l][r][k] != -1:
		return dp[l][r][k]

	# Finding cost
	cost = ((ord(X[l]) - ord('a')) ^
			(ord(Y[r]) - ord('a')))

	dp[l][r][k] = min([cost + solve(X, Y, l - 1,
										r - 1, k - 1, dp),
							solve(X, Y, l - 1, r, k, dp),
							solve(X, Y, l, r - 1, k, dp)])

	return dp[l][r][k]

# Driver Code
if __name__ == "__main__":
	X = "abble"
	Y = "pie"
	n = len(X)
	m = len(Y)
	k = 2
	dp = [[[-1] * N for __ in range(N)]
					for ___ in range(N)]
	ans = solve(X, Y, n - 1, m - 1, k, dp)

	print(-1 if ans == 1000000000 else ans)
