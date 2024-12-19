# Python3 program to find length
# of the longest geometric
# progression in a given sett

# Returns length of the longest GP
# subset of sett[]

def lenOfLongestGP(sett, n):
	# Base cases
	if n < 2:
		return n
	if n == 2:
		return 2 if (sett[1] % sett[0] == 0) else 1
	# let us sort the sett first
	sett.sort()

	# An entry L[i][j] in this
	# table stores LLGP with
	# sett[i] and sett[j] as first
	# two elements of GP
	# and j > i.
	L = [[0 for i in range(n)] for i in range(n)]

	# Initialize result (A single
	# element is always a GP)
	llgp = 1

	# Initialize values of last column
	for i in range(0, n-1):
		if sett[n-1] % sett[i] == 0:
			L[i][n-1] = 2
			if 2 > llgp:
				llgp = 2
		else:
			L[i][n-1] = 1
	L[n-1][n-1] = 1

	# Consider every element as second element of GP
	for j in range(n-2, 0, -1):

		# Search for i and k for j
		i = j - 1
		k = j + 1
		while i >= 0 and k <= n - 1:

			# Two cases when i, j and k don't form
			# a GP.
			if sett[i] * sett[k] < sett[j] * sett[j]:
				k += 1
			elif sett[i] * sett[k] > sett[j] * sett[j]:
				if sett[j] % sett[i] == 0:
					L[i][j] = 2
				else:
					L[i][j] = 1
				i -= 1

			# i, j and k form GP, LLGP with i and j as
			# first two elements is equal to LLGP with
			# j and k as first two elements plus 1.
			# L[j][k] must have been filled before as
			# we run the loop from right side
			else:
				if sett[j] % sett[i] == 0:
					L[i][j] = L[j][k] + 1

					# Update overall LLGP
					if L[i][j] > llgp:
						llgp = L[i][j]
				else:
					L[i][j] = 1

				# Change i and k to fill more L[i][j]
				# values for current j
				i -= 1
				k += 1

		# If the loop was stopped due to k becoming
		# more than n-1, set the remaining entries
		# in column j as 1 or 2 based on divisibility
		# of sett[j] by sett[i]
		while i >= 0:
			if sett[j] % sett[i] == 0:
				L[i][j] = 2
			else:
				L[i][j] = 1
			i -= 1

	return llgp


# Driver code
if __name__ == '__main__':
	set1 = [1, 3, 9, 27, 81, 243]
	n1 = len(set1)
	print(lenOfLongestGP(set1, n1))

	set2 = [1, 3, 4, 9, 7, 27]
	n2 = len(set2)
	print(lenOfLongestGP(set2, n2))

	set3 = [2, 3, 5, 7, 11, 13]
	n3 = len(set3)
	print(lenOfLongestGP(set3, n3))

# this code is contributed by sahilshelangia
