# A dynamic programming based Python program
# to find shortest uncommon subsequence.
MAX = 1005

# Returns length of shortest common subsequence
def shortestSeq(S: list, T: list):
	m = len(S)
	n = len(T)

	# declaring 2D array of m + 1 rows and
	# n + 1 columns dynamically
	dp = [[0 for i in range(n + 1)]
			for j in range(m + 1)]

	# T string is empty
	for i in range(m + 1):
		dp[i][0] = 1

	# S string is empty
	for i in range(n + 1):
		dp[0][i] = MAX

	for i in range(1, m + 1):
		for j in range(1, n + 1):
			ch = S[i - 1]
			k = j - 1
			while k >= 0:
				if T[k] == ch:
					break
				k -= 1

			# char not present in T
			if k == -1:
				dp[i][j] = 1
			else:
				dp[i][j] = min(dp[i - 1][j],
							dp[i - 1][k] + 1)

	ans = dp[m][n]
	if ans >= MAX:
		ans = -1

	return ans

# Driver Code
if __name__ == "__main__":
	S = "babab"
	T = "babba"

	print("Length of shortest subsequence is:",shortestSeq(S, T))
