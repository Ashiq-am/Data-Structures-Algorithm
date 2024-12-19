# Python program to find a range of composite
# numbers of given length

# function to calculate factorial
def factorial(n):
	a = 1
	for i in range(2, n + 1):
		a *= i
	return a

# to print range of length n
# having all composite integers
def printRange(n):
	a = factorial(n + 2) + 2
	b = a + n - 1
	print("["+str(a)+", "+str(b)+"]")

# driver code to test above functions
n = 3
printRange(n)
