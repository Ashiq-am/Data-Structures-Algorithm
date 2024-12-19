# Simple Python program
# to compute x * (2^n)

# Returns 2 raised to power n
def power2(n):

	if (n == 0):
		return 1
	if (n == 1):
		return 2
	return power2(n / 2) * power2(n / 2)


def multiply(x, n):
	return x * power2(n);


# Driven program
x = 70
n = 2
print(multiply(x, n))

# This code is contributed by Smitha Dinesh Semwal
