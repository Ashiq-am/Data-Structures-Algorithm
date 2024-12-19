# A Dynamic programming based Python program
# to find maximum sum by recursively breaking
# a number in 3 parts.

MAX = 1000000

def breakSum(n):

	dp = [0]*(n+1)

	# base conditions
	dp[0] = 0
	dp[1] = 1

	# Fill in bottom-up manner using recursive
	# formula.
	for i in range(2, n+1):
		dp[i] = max(dp[int(i/2)] + dp[int(i/3)] + dp[int(i/4)], i);

	return dp[n]


# Driver program to run the case
n = 24
print(breakSum(n))
