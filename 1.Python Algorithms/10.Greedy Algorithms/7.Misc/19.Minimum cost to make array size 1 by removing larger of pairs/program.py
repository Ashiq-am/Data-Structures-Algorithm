# Python program to find minimum
# cost to reduce array size to 1

# function to calculate the
# minimum cost
def cost(a, n):

	# Minimum cost is n-1 multiplied
	# with minimum element.
	return ( (n - 1) * min(a) )


# driver code
a = [ 4, 3, 2 ]
n = len(a)
print(cost(a, n))
