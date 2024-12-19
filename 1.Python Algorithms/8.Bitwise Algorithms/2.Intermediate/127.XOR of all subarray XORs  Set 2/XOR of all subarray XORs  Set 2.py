# Python 3 program to get total xor
# of all subarray xors

# Returns XOR of all subarray xors
def getTotalXorOfSubarrayXors(arr, N):

	# if even number of terms are there,
	# all numbers will appear even number
	# of times. So result is 0.
	if (N % 2 == 0):
		return 0

	# else initialize result by 0
	# as (a xor 0 = a)
	res = 0
	for i in range(0, N, 2):
		res ^= arr[i]

	return res

# Driver code
if __name__ == "__main__":

	arr = [3, 5, 2, 4, 6]
	N = len(arr)
	print(getTotalXorOfSubarrayXors(arr, N))

# This code is contributed by ita_c
