# Python3 program to find maximum pair sum
# whose difference is less than K

# Method to return maximum sum we can
# get by finding less than K difference
# pairs


def maxSumPairWithDifferenceLessThanK(arr, N, k):

	maxSum = 0

	# Sort elements to ensure every i and
	# i-1 is closest possible pair
	arr.sort()

	# To get maximum possible sum, iterate
	# from largest to smallest, giving larger
	# numbers priority over smaller numbers.
	i = N - 1
	while (i > 0):

		# Case I: Diff of arr[i] and arr[i-1]
		#	 is less then K, add to maxSum
		# Case II: Diff between arr[i] and
		#	 arr[i-1] is not less then K,
		#	 move to next i since with sorting
		#	 we know, arr[i]-arr[i-1] < arr[i]-arr[i-2]
		#	 and so on.
		if (arr[i] - arr[i - 1] < k):

			# Assuming only positive numbers.
			maxSum += arr[i]
			maxSum += arr[i - 1]

			# When a match is found skip this pair
			i -= 1
		i -= 1

	return maxSum


# Driver Code
arr = [3, 5, 10, 15, 17, 12, 9]
N = len(arr)

K = 4
print(maxSumPairWithDifferenceLessThanK(arr, N, K))
