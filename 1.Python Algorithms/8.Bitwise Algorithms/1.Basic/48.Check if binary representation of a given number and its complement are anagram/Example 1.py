# Python3 program to check if binary
# representations of a number and it's
# complement are anagram.

ULL_SIZE = 8 * 8

def isComplementAnagram(a):

	# Find reverse binary representation of a.
	binary_a = [0 for _ in range(ULL_SIZE)]
	binary_b = [0 for _ in range(ULL_SIZE)]

	i = 0
	while a > 0:

		binary_a[i] = a % 2
		a = int(a / 2)
		i += 1

	# Find reverse binary representation
	# of complement.
	for i in range(ULL_SIZE):
		binary_b[i] = 1 - binary_a[i]

	# Sort binary representations and compare
	# after sorting.
	binary_a.sort()
	binary_b.sort()

	for i in range(ULL_SIZE):
		if (binary_a[i] != binary_b[i]):
			return 0

	return 1

# Driver code
a = 4294967295
print(isComplementAnagram(a))

# This code is contributed by phasing17
