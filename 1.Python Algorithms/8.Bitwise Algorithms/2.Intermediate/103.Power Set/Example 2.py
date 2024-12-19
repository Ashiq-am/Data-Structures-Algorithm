# Python3 program for the above approach

# A function which gives previous
# permutation of the array
# and returns true if a permutation
# exists.
def prev_permutation(str):

	# Find index of the last
	# element of the string
	n = len(str) - 1

	# Find largest index i such
	# that str[i - 1] > str[i]
	i = n
	while (i > 0 and str[i - 1] <= str[i]):
		i -= 1

	# If string is sorted in
	# ascending order we're
	# at the last permutation
	if (i <= 0):
		return False

	# Note - str[i..n] is sorted
	# in ascending order Find
	# rightmost element's index
	# that is less than str[i - 1]
	j = i - 1
	while (j + 1 <= n and str[j + 1] < str[i - 1]):
		j += 1

	# Swap character at i-1 with j
	temper = str[i - 1]
	str[i - 1] = str[j]
	str[j] = temper

	# Reverse the substring [i..n]
	size = n-i+1
	for idx in range(int(size / 2)):
		temp = str[idx + i]
		str[idx + i] = str[n - idx]
		str[n - idx] = temp

	return True

# Function to print all the power set
def printPowerSet(set, n):

	contain = [0 for _ in range(n)]

	# Empty subset
	print()

	for i in range(n):
		contain[i] = 1

		# To avoid changing original 'contain'
		# array creating a copy of it i.e.
		# "Contain"
		Contain = contain.copy()

		# All permutation
		while True:
			for j in range(n):
				if (Contain[j]):
					print(set[j], end="")
			print()
			if not prev_permutation(Contain):
				break

# Driver code
set = ['a', 'b', 'c']
printPowerSet(set, 3)

# This code is contributed by phasing17
