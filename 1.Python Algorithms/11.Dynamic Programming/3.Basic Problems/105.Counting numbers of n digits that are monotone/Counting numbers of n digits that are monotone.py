# Python3 program to count numbers of n
# digits that are monotone.

# Considering all possible digits as
# {1, 2, 3, ..9}
DP_s = 9

def getNumMonotone(ln):

	# DP[i][j] is going to store monotone
	# numbers of length i+1 considering
	# j+1 digits.
	DP = [[0]*DP_s for i in range(ln)]

	# Unit length numbers
	for i in range(DP_s):
		DP[0][i] = i + 1

	# Single digit numbers
	for i in range(ln):
		DP[i][0] = 1

	# Filling rest of the entries
	# in bottom up manner.
	for i in range(1, ln):

		for j in range(1, DP_s):
			DP[i][j] = DP[i - 1][j] + DP[i][j - 1]

	return DP[ln - 1][DP_s - 1]


# Driver code
print(getNumMonotone(10))
