# Python3 program to find the Kth
# smallest element after
# removing some integer from
# first n natural number.

# Return the K-th
# smallest element.
def ksmallest(arr, n, k):

	arr.sort()

	# Checking if k lies
	# before 1st element
	if (k < arr[0]):
		return k

	# If k is the first
	# element of array arr[].
	if (k == arr[0]):
		return arr[0] + 1

	# If k is more
	# than last element
	if (k > arr[n - 1]):
		return k + n

	# If first element
	# of array is 1.
	if (arr[0] == 1):
		k-= 1

	# Reducing k by numbers
	# before arr[0].
	else:
		k -= (arr[0] - 1)

	# Finding k'th smallest element
	# after removing array elements.
	for i in range(1, n):
		# Finding count of element between
		# i-th and (i-1)-th element.
		c = arr[i] - arr[i - 1] - 1
		if (k <= c):
			return arr[i - 1] + k
		else:
			k -= c

	return arr[n - 1] + k

# Driver Code
k = 1
arr =[ 1 ]
n = len(arr)
print(ksmallest(arr, n, k))


