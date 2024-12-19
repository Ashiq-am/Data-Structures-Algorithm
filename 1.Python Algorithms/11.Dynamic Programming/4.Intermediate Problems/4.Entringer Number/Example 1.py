# Python Program to find Entringer Number E(n, k)

# Return Entringer Number E(n, k)
def zigzag(n, k):

	# Base Case
	if (n == 0 and k == 0):
		return 1

	# Base Case
	if (k == 0):
		return 0

	# Recursive step
	return zigzag(n, k - 1) + zigzag(n - 1, n - k);

# Driven Program
n = 4
k = 3
print(zigzag(n, k))
