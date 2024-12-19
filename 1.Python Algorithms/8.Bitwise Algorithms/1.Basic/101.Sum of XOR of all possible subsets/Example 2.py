# Python3 approach to finding the XOR_SUM

# Returns sum of XORs of all subsets
def xorSum(arr, n):

	bits = 0

	# Finding bitwise OR of all elements
	for i in range(n):
		bits |= arr[i]

	ans = bits * pow(2, n-1)

	return ans

# Driver Code
arr = [1, 5, 6]
size = len(arr)
print(xorSum(arr, size))

# This code is contributed by Anant Agarwal.
