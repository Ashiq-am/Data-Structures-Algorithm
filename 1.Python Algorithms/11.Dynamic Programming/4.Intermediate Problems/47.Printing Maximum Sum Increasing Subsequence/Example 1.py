# Dynamic Programming solution to construct
# Maximum Sum Increasing Subsequence */

# Utility function to calculate sum of all
# vector elements


def findSum(arr):

	summ = 0
	for i in arr:
		summ += i
	return summ

# Function to construct Maximum Sum Increasing
# Subsequence


def printMaxSumIS(arr, n):

	# L[i] - The Maximum Sum Increasing
	# Subsequence that ends with arr[i]
	L = [[] for i in range(n)]

	# L[0] is equal to arr[0]
	L[0].append(arr[0])

	# start from index 1
	for i in range(1, n):

		# for every j less than i
		for j in range(i):

			# L[i] = {MaxSum(L[j])} + arr[i]
			# where j < i and arr[j] < arr[i]
			if ((arr[i] > arr[j]) and
					(findSum(L[i]) < findSum(L[j]))):
				for e in L[j]:
					if e not in L[i]:
						L[i].append(e)

		# L[i] ends with arr[i]
		L[i].append(arr[i])

		# L[i] now stores Maximum Sum Increasing
		# Subsequence of arr[0..i] that ends with
		# arr[i]

	res = L[0]

	# find max
	for x in L:
		if (findSum(x) > findSum(res)):
			res = x

	# max will contain result
	for i in res:
		print(i, end=" ")


# Driver Code
arr = [3, 2, 6, 4, 5, 1]
n = len(arr)

# construct and prMax Sum IS of arr
printMaxSumIS(arr, n)
