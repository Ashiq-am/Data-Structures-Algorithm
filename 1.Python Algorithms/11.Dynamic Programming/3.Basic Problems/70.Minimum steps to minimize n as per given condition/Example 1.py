# Python program to minimize
# n to 1 by given
# rule in minimum steps

# function to calculate min steps
def getMinSteps(n, memo):

	# base case
	if (n == 1):
		return 0
	if (memo[n] != -1):
		return memo[n]

	# store temp value for n as min(f(n-1),
	# f(n//2), f(n//3)) + 1
	res = getMinSteps(n-1, memo)

	if (n%2 == 0):
		res = min(res, getMinSteps(n//2, memo))
	if (n%3 == 0):
		res = min(res, getMinSteps(n//3, memo))

	# store memo[n] and return
	memo[n] = 1 + res
	return memo[n]

# This function mainly
# initializes memo[] and
# calls getMinSteps(n, memo)
def getsMinSteps(n):

	memo = [0 for i in range(n+1)]

	# initialize memoized array
	for i in range(n+1):
		memo[i] = -1

	return getMinSteps(n, memo)

# driver program
n = 10
print(getsMinSteps(n))
