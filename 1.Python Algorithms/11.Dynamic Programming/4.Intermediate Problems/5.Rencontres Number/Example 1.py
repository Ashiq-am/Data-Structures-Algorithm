# Recursive CPP program to find
# n-th Rencontres Number

# Returns value of Binomial Coefficient C(n, k)
def binomialCoeff(n, k):

	# Base Cases
	if (k == 0 or k == n):
		return 1

	# Recurrence relation
	return (binomialCoeff(n - 1, k - 1)
		+ binomialCoeff(n - 1, k))

# Return Recontres number D(n, m)
def RencontresNumber(n, m):

	# base condition
	if (n == 0 and m == 0):
		return 1

	# base condition
	if (n == 1 and m == 0):
		return 0

	# base condition
	if (m == 0):
		return ((n - 1) * (RencontresNumber(n - 1, 0)
						+ RencontresNumber(n - 2, 0)))

	return (binomialCoeff(n, m) *
			RencontresNumber(n - m, 0))

# Driver Program
n = 7; m = 2
print(RencontresNumber(n, m))
