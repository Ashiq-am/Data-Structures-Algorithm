# unsets the rightmost set bit
# of n and returns the result
def fun(n):

	return n & (n-1)

# Driver code

n = 7
print("The number after unsetting the rightmost set bit", fun(n))

# This code is contributed
# by Anant Agarwal.
