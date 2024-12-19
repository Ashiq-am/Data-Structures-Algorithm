# Python 3 program to counts Palindromic
# Subsequence in a given String using recursion

str = "abcb"

# Function return the total
# palindromic subsequence


def countPS(i, j):

	if(i > j):
		return 0

	if(dp[i][j] != -1):
		return dp[i][j]

	if(i == j):
		dp[i][j] = 1
		return dp[i][j]

	elif (str[i] == str[j]):
		dp[i][j] = (countPS(i + 1, j) +
					countPS(i, j - 1) + 1)
		return dp[i][j]
	else:
		dp[i][j] = (countPS(i + 1, j) +
					countPS(i, j - 1) -
					countPS(i + 1, j - 1))
		return dp[i][j]


# Driver code
if __name__ == "__main__":

	dp = [[-1 for x in range(1000)]
		for y in range(1000)]

	n = len(str)
	print("Total palindromic subsequence are :",
		countPS(0, n - 1))
