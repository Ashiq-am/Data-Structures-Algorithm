# Python3 program to find maximum array
# sum after at most k negations


def sol(arr, k):

	# Sorting given array using
	# in-built java sort function
	arr.sort()

	Sum = 0
	i = 0

	while (k > 0):

		# If we find a 0 in our
		# sorted array, we stop
		if (arr[i] >= 0):
			k = 0
		else:
			arr[i] = (-1) * arr[i]
			k = k - 1

		i += 1

	# Calculating sum
	for j in range(len(arr)):
		Sum += arr[j]

	return Sum


# Driver code
arr = [-2, 0, 5, -1, 2]

print(sol(arr, 4))
