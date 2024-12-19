# Python3 program to maximize the sum of difference
# between consecutive elements in circular array

# Return the maximum Sum of difference
# between consecutive elements
def maxSum(arr, n):
	sum = 0

	# Sorting the array
	arr.sort()

	# Subtracting a1, a2, a3,....., a(n/2)-1, an/2
	# twice and adding a(n/2)+1, a(n/2)+2, a(n/2)+3,.
	# ...., an - 1, an twice.
	for i in range(0, int(n / 2)) :
		sum -= (2 * arr[i])
		sum += (2 * arr[n - i - 1])

	return sum


# Driver Program
arr = [4, 2, 1, 8]
n = len(arr)
print (maxSum(arr, n))
