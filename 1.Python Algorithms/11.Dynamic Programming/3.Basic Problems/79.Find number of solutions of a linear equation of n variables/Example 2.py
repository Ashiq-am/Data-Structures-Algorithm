# A Dynamic Programming based
# Python program to find number
# of non-negative solutions for
# a given linear equation

# Returns count of solutions for given
# rhs and coefficients coeff[0...n-1]
def countSol(coeff, n, rhs):

	# Create and initialize a table
	# to store results of subproblems
	dp = [0 for i in range(rhs + 1)]
	dp[0] = 1

	# Fill table in bottom up manner
	for i in range(n):
		for j in range(coeff[i], rhs + 1):
			dp[j] += dp[j - coeff[i]]

	return dp[rhs]

# Driver Code
coeff = [2, 2, 5]
rhs = 4
n = len(coeff)
print(countSol(coeff, n, rhs))
