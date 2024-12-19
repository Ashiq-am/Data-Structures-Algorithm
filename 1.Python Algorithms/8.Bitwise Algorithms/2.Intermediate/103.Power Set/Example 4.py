# Python3 program to implement the approach

# Function to build the power sets
def findPowerSet(s, res, n):
	if (n == 0):
		for i in res:
			print(i, end="")
		print()
		return

	# append the subset to result
	res.append(s[n - 1])
	findPowerSet(s, res, n - 1)
	res.pop()
	findPowerSet(s, res, n - 1)

# Function to print the power set
def printPowerSet(s, n):
	ans = []
	findPowerSet(s, ans, n)

# Driver code
set = ['a', 'b', 'c']
printPowerSet(set, 3)

# This code is contributed by phasing17
