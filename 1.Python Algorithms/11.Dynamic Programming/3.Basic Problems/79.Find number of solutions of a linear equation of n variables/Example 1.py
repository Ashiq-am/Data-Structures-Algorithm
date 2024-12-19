# A naive recursive Python program
# to find number of non-negative
# solutions for a given linear equation

# Recursive function that returns
# count of solutions for given rhs
# value and coefficients coeff[stat...end]
def countSol(coeff, start, end, rhs):

	# Base case
	if (rhs == 0):
		return 1

	# Initialize count of solutions
	result = 0

	# One by one subtract all smaller or
	# equal coefficients and recur
	for i in range(start, end+1):
		if (coeff[i] <= rhs):
			result += countSol(coeff, i, end,
							rhs - coeff[i])

	return result

# Driver Code
coeff = [2, 2, 5]
rhs = 4
n = len(coeff)
print(countSol(coeff, 0, n - 1, rhs))
