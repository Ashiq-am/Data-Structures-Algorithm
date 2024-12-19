# Program to find minimum cost for pyramid
# from given array

# Returns minimum cost to form a pyramid
def minPyramidCost(arr: list, N):

	# Store the maximum possible pyramid height
	left = [0] * N
	right = [0] * N

	# Maximum height at start is 1
	left[0] = min(arr[0], 1)

	# For each position calculate maximum height
	for i in range(1, N):
		left[i] = min(arr[i],
				min(left[i - 1] + 1, i + 1))

	# Maximum height at end is 1
	right[N - 1] = min(arr[N - 1], 1)

	# For each position calculate maximum height
	for i in range(N - 2, -1, -1):
		right[i] = min(arr[i],
				min(right[i + 1] + 1, N - i))

	# Find minimum possible among calculated values
	tot = [0] * N
	for i in range(N):
		tot[i] = min(right[i], left[i])

	# Find maximum height of pyramid
	max_ind = 0
	for i in range(N):
		if tot[i] > tot[max_ind]:
			max_ind = i

	# Calculate cost of this pyramid
	cost = 0
	height = tot[max_ind]

	# Calculate cost of left half
	for x in range(max_ind, -1, -1):
		cost += arr[x] - height
		if height > 0:
			height -= 1

	# Calculate cost of right half
	height = tot[max_ind] - 1
	for x in range(max_ind + 1, N):
		cost += arr[x] - height
		if height > 0:
			height -= 1

	return cost

# Driver Code
if __name__ == "__main__":
	arr = [1, 2, 3, 4, 2, 1]
	N = len(arr)
	print(minPyramidCost(arr, N))
