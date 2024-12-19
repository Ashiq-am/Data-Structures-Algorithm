# Python3 program to find maximum
# product of a subset.

# def to find maximum
# product of a subset


def minProductSubset(a, n):
	if (n == 1):
		return a[0]

	# Find count of negative numbers,
	# count of zeros, maximum valued
	# negative number, minimum valued
	# positive number and product
	# of non-zero numbers
	max_neg = float('-inf')
	min_pos = float('inf')
	count_neg = 0
	count_zero = 0
	prod = 1
	for i in range(0, n):

		# If number is 0, we don't
		# multiply it with product.
		if (a[i] == 0):
			count_zero = count_zero + 1
			continue

		# Count negatives and keep
		# track of maximum valued
		# negative.
		if (a[i] < 0):
			count_neg = count_neg + 1
			max_neg = max(max_neg, a[i])

		# Track minimum positive
		# number of array
		if (a[i] > 0):
			min_pos = min(min_pos, a[i])

		prod = prod * a[i]

	# If there are all zeros
	# or no negative number
	# present
	if (count_zero == n or (count_neg == 0
							and count_zero > 0)):
		return 0

	# If there are all positive
	if (count_neg == 0):
		return min_pos

	# If there are even number of
	# negative numbers and count_neg
	# not 0
	if ((count_neg & 1) == 0 and
			count_neg != 0):

		# Otherwise result is product of
		# all non-zeros divided by
		# maximum valued negative.
		prod = int(prod / max_neg)

	return prod


# Driver code
a = [-1, -1, -2, 4, 3]
n = len(a)
print(minProductSubset(a, n))

