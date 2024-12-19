# Python program to find n-th stair
# using step size 1 or 2 or 3.

# A recursive function used by countWays


def countWays(n):
	res = [0] * (n + 2)
	res[0] = 1
	res[1] = 1
	res[2] = 2

	for i in range(3, n + 1):
		res[i] = res[i - 1] + res[i - 2] + res[i - 3]

	return res[n]


# Driver code
n = 4
print(countWays(n))
