# Python program to evaluate ceil(7n/8) without using * and /


def multiplyBySevenByEight(n):

	# Note the inner bracket here. This is needed
	# because precedence of '-' operator is higher
	# than '<<'
	return (n - (n >> 3))


# Driver program to test above function */
n = 9
print(multiplyBySevenByEight(n))

# This code is contributed by
# Smitha Dinesh Semwal
