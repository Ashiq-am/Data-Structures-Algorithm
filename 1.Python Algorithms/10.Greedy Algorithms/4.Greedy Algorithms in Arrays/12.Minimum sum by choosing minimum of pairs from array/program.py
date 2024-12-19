# Python code for minimum cost of
# array minimization

# Function defintion for minCost
def minSum(A):

	# find the minimum element of A[]
	min_val = min(A)

	# return the answer
	return min_val * (len(A)-1)

# driver code
A = [7, 2, 3, 4, 5, 6]
print (minSum(A))
