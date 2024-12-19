# A tail recursive function
# to calculate factorial
def fact(n, a = 1):

	if (n == 0):
		return a

	return fact(n - 1, n * a)

# Driver program to test
# above function
print(fact(5))


