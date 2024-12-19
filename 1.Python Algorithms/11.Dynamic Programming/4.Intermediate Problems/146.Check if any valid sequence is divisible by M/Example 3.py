# Python3 Program to Check if any
# valid sequence is divisible by M
MAX = 100

def isPossible(n, index, modulo,
					M, arr, dp):

	# Calculate modulo for this call
	modulo = ((modulo % M) + M) % M

	# Base case
	if (index == n):

		# check if sum is divisible by M
		if (modulo == 0):
			return 1
		return 0

	# check if the current state is
	# already computed
	if (dp[index][modulo] != -1):
		return dp[index][modulo]

	# 1.Try placing '+'
	placeAdd = isPossible(n, index + 1, modulo +
						arr[index], M, arr, dp)

	# 2. Try placing '-'
	placeMinus = isPossible(n, index + 1, modulo -
							arr[index], M, arr, dp)

	# calculate value of res
	# for recursive case
	res = bool(placeAdd or placeMinus)

	# store the value for res for current
	# states and return for parent call
	dp[index][modulo] = res
	return res

# Driver code
arr = [ 1, 2, 3, 4, 6 ]
n = len(arr)
M = 4

# MAX is the Maximum value
# M can take
dp = [[-1] * (n + 1)] * MAX

res = isPossible(n, 1, arr[0],
				M, arr, dp)

if(res == True):
	print("True")
else:
	print("False")
