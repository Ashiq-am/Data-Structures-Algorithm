# Python program to find
# if given string is K-Palindrome
# or not

# Returns length of LCS
# for X[0..m-1], Y[0..n-1]
def lcs(X, Y, m, n ):

	L = [[0]*(n+1) for _ in range(m+1)]

	# Following steps build
		# L[m+1][n+1] in bottom up
		# fashion. Note that L[i][j]
		# contains length of
	# LCS of X[0..i-1] and Y[0..j-1]
	for i in range(m+1):
		for j in range(n+1):
			if not i or not j:
				L[i][j] = 0
			elif X[i - 1] == Y[j - 1]:
				L[i][j] = L[i - 1][j - 1] + 1
			else:
				L[i][j] = max(L[i - 1][j], L[i][j - 1])

	# L[m][n] contains length
		# of LCS for X and Y
	return L[m][n]

# find if given string is
# K-Palindrome or not
def isKPal(string, k):

	n = len(string)

	# Find reverse of string
	revStr = string[::-1]

	# find longest palindromic
		# subsequence of
	# given string
	lps = lcs(string, revStr, n, n)

	# If the difference between
		# longest palindromic
	# subsequence and the original
		# string is less
	# than equal to k, then
		# the string is k-palindrome
	return (n - lps <= k)

# Driver program
string = "abcdeca"
k = 2

print("Yes" if isKPal(string, k) else "No")
