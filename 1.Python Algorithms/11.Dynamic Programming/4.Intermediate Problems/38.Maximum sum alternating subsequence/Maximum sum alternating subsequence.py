# Python3 program to find sum of maximum
# sum alternating sequence starting with
# first element.

# Return sum of maximum sum alternating
# sequence starting with arr[0] and is
# first decreasing.


def maxAlternateSum(arr, n):

	if (n == 1):
		return arr[0]
	min = arr[0]
	for i in range(1, n):
		if(min > arr[i]):
			min = arr[i]
	if(arr[0] == min):
		return arr[0]
	# Create two empty array that
	# store result of maximum sum
	# of alternate sub-sequence

	# Stores sum of decreasing and
	# increasing sub-sequence
	dec = [0 for i in range(n + 1)]

	# store sum of increasing and
	# decreasing sun-sequence
	inc = [0 for i in range(n + 1)]

	# As per question, first element
	# must be part of solution.
	dec[0] = inc[0] = arr[0]

	flag = 0

	# Traverse remaining elements of array
	for i in range(1, n):

		for j in range(i):

			# IF current sub-sequence is decreasing the
			# update dec[j] if needed. dec[i] by current
			# inc[j] + arr[i]
			if (arr[j] > arr[i]):

				dec[i] = max(dec[i], inc[j] + arr[i])

				# Revert the flag, if first
				# decreasing is found
				flag = 1

			# If next element is greater but flag should be 1
			# i.e. this element should be counted after the
			# first decreasing element gets counted
			elif (arr[j] < arr[i] and flag == 1):

				# If current sub-sequence is
				# increasing then update inc[i]
				inc[i] = max(inc[i], dec[j] + arr[i])

	# Find maximum sum in b/w inc[] and dec[]
	result = -2147483648
	for i in range(n):

		if (result < inc[i]):
			result = inc[i]
		if (result < dec[i]):
			result = dec[i]

	# Return maximum sum
	# alternate sun-sequence
	return result


# Driver program
arr = [8, 2, 3, 5, 7, 9, 10]
n = len(arr)
print("Maximum sum = ",
	maxAlternateSum(arr, n))
