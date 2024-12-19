# Python program to calculate minimum sum of product
# of two arrays.

# Returns minimum sum of product of two arrays
# with permutations allowed


def minValue(A, B, n):

	# Sort A and B so that minimum and maximum
	# value can easily be fetched.
	A.sort()
	B.sort()

	# Multiplying minimum value of A and maximum
	# value of B
	result = 0
	for i in range(n):
		result += (A[i] * B[n - i - 1])

	return result


# Driven Program
A = [3, 1, 1]
B = [6, 5, 4]
n = len(A)
print(minValue(A, B, n))


