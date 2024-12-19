# Python3 code to find minimum cost to make two strings
# identical

# Function to returns cost of removing the identical
# characters in LCS for X[0..m-1], Y[0..n-1]
def lcs(X, Y, m, n):
	L=[[0 for i in range(n+1)]for i in range(m+1)]

	# Following steps build L[m+1][n+1] in bottom
	# up fashion. Note that L[i][j] contains cost
	# of removing identical characters in LCS of
	# X[0..i-1] and Y[0..j-1]
	for i in range(m+1):
		for j in range(n+1):
			if (i == 0 or j == 0):
				L[i][j] = 0

			# If both characters are same, add both
			# of them
			elif (X[i - 1] == Y[j - 1]):
				L[i][j] = L[i - 1][j - 1] + 2 * (ord(X[i - 1]) - 48)

			# Otherwise find the maximum cost among them
			else:
				L[i][j] = max(L[i - 1][j], L[i][j - 1])
	return L[m][n]

# Returns cost of making X[] and Y[] identical
def findMinCost( X, Y):
	# Find LCS of X[] and Y[]
	m = len(X)
	n = len(Y)
	# Initialize the cost variable
	cost = 0

	# Find cost of all acters in
	# both strings
	for i in range(m):
		cost += ord(X[i]) - 48

	for i in range(n):
		cost += ord(Y[i]) - 48
	ans=cost - lcs(X, Y, m, n)
	return ans

# Driver program to test above function
X = "3759"
Y = "9350"
print("Minimum Cost to make two strings ","identical is = " ,findMinCost(X, Y))
