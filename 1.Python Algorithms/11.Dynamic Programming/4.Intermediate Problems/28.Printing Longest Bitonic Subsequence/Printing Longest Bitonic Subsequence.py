# Dynamic Programming solution to print Longest
# Bitonic Subsequence


def _print(arr: list, size: int):
	for i in range(size):
		print(arr[i], end=" ")


# Function to construct and print Longest
# Bitonic Subsequence
def printLBS(arr: list, n: int):

	# LIS[i] stores the length of the longest
	# increasing subsequence ending with arr[i]
	LIS = [0] * n
	for i in range(n):
		LIS[i] = []

	# initialize LIS[0] to arr[0]
	LIS[0].append(arr[0])

	# Compute LIS values from left to right
	for i in range(1, n):

		# for every j less than i
		for j in range(i):

			if ((arr[j] < arr[i]) and (len(LIS[j]) > len(LIS[i]))):
				LIS[i] = LIS[j].copy()

		LIS[i].append(arr[i])

	# LIS[i] now stores Maximum Increasing
	# Subsequence of arr[0..i] that ends with
	# arr[i]

	# LDS[i] stores the length of the longest
	# decreasing subsequence starting with arr[i]
	LDS = [0] * n
	for i in range(n):
		LDS[i] = []

	# initialize LDS[n-1] to arr[n-1]
	LDS[n - 1].append(arr[n - 1])

	# Compute LDS values from right to left
	for i in range(n - 2, -1, -1):

		# for every j greater than i
		for j in range(n - 1, i, -1):

			if ((arr[j] < arr[i]) and (len(LDS[j]) > len(LDS[i]))):
				LDS[i] = LDS[j].copy()

		LDS[i].append(arr[i])

	# reverse as vector as we're inserting at end
	for i in range(n):
		LDS[i] = list(reversed(LDS[i]))

	# LDS[i] now stores Maximum Decreasing Subsequence
	# of arr[i..n] that starts with arr[i]

	max = 0
	maxIndex = -1

	for i in range(n):

		# Find maximum value of size of LIS[i] + size
		# of LDS[i] - 1
		if (len(LIS[i]) + len(LDS[i]) - 1 > max):

			max = len(LIS[i]) + len(LDS[i]) - 1
			maxIndex = i

	# print all but last element of LIS[maxIndex] vector
	_print(LIS[maxIndex], len(LIS[maxIndex]) - 1)

	# print all elements of LDS[maxIndex] vector
	_print(LDS[maxIndex], len(LDS[maxIndex]))


# Driver Code
if __name__ == "__main__":

	arr = [1, 11, 2, 10, 4, 5, 2, 1]
	n = len(arr)

	printLBS(arr, n)
