# Python program for painter's partition problem

# Find minimum required painters for given maxlen
# which is the maximum length a painter can paint
def numberOfPainters(arr, n, maxLen):
	total = 0
	numPainters = 1

	for i in arr:
		total += i

		if (total > maxLen):

			# for next count
			total = i
			numPainters += 1

	return numPainters

def partition(arr, n, k):
	lo = max(arr)
	hi = sum(arr)

	while (lo < hi):
		mid = lo + (hi - lo) / 2
		requiredPainters = numberOfPainters(arr, n, mid)

		# find better optimum in lower half
		# here mid is included because we
		# may not get anything better
		if (requiredPainters <= k):
			hi = mid

		# find better optimum in upper half
		# here mid is excluded because it gives
		# required Painters > k, which is invalid
		else:
			lo = mid + 1

	# required
	return lo

# Driver code
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(arr)
k = 3
print(int(partition(arr, n, k)))
