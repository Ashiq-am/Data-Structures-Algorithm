# A Python3 memoization based recursive
# program to count numbers with Sum of n
# as given 'Sum'

# A lookup table used for memoization
lookup = [[-1 for i in range(501)]
			for i in range(101)]

# Memoization based implementation
# of recursive function
def countRec(n, Sum):

	# Base case
	if (n == 0):
		return Sum == 0

	# If this subproblem is already evaluated,
	# return the evaluated value
	if (lookup[n][Sum] != -1):
		return lookup[n][Sum]

	# Initialize answer
	ans = 0

	# Traverse through every digit and
	# recursively count numbers beginning
	# with it
	for i in range(10):
		if (Sum-i >= 0):
			ans += countRec(n - 1, Sum-i)
	lookup[n][Sum] = ans

	return lookup[n][Sum]

# This is mainly a wrapper over countRec. It
# explicitly handles leading digit and calls
# countRec() for remaining n.
def finalCount(n, Sum):

	# Initialize final answer
	ans = 0

	# Traverse through every digit from 1 to
	# 9 and count numbers beginning with it
	for i in range(1, 10):
		if (Sum - i >= 0):
			ans += countRec(n - 1, Sum - i)
	return ans

# Driver Code
n, Sum = 3, 5
print(finalCount(n, Sum))
