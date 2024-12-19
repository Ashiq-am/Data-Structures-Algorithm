# Python program to find
# XOR of XOR's of all subsets

# Returns XOR of all
# XOR's of given subset


def findXOR(Set, n):

	# XOR is 1 only when
	# n is 1, else 0
	if (n == 1):
		return Set[0]
	else:
		return 0

# Driver code


Set = [1, 2, 3]
n = len(Set)

print("XOR of XOR's of all subsets is ",
	findXOR(Set, n))

# This code is contributed
# by Anant Agarwal.
