# Python3 program using to find length of
# the longest common substring recursion

# Returns length of function for longest
# common substring of X[0..m-1] and Y[0..n-1]


def lcs(i, j, count):

	if (i == 0 or j == 0):
		return count

	if (X[i - 1] == Y[j - 1]):
		count = lcs(i - 1, j - 1, count + 1)

	count = max(count, max(lcs(i, j - 1, 0),
						lcs(i - 1, j, 0)))

	return count


# Driver code
if __name__ == "__main__":

	X = "abcdxyz"
	Y = "xyzabcd"

	n = len(X)
	m = len(Y)

	print(lcs(n, m, 0))
