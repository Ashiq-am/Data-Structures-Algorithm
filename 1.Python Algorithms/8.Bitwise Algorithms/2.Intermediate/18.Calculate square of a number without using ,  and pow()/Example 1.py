# Simple solution to
# calculate square without
# using * and pow()

def square(n):

	# handle negative input
	if (n < 0):
		n = -n

	# Initialize result
	res = n

	# Add n to res n-1 times
	for i in range(1, n):
		res += n

	return res


# Driver Code
for n in range(1, 6):
	print("n =", n, end=", ")
	print("n^2 =", square(n))

# This code is contributed by
# Smitha Dinesh Semwal
