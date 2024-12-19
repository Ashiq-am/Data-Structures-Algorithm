# Python 3 program to
# print all bitwise
# subsets of N
# (Efficient approach)

# function to find
# bitwise subsets
# Efficient approach
def printSubsets(n):
	i=n
	while(i != 0):
		print(i,end=" ")
		i=(i - 1) & n
	print("0")

# Driver Code
n = 9
printSubsets(n)
