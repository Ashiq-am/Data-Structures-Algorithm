# Python3 program to count number
# of rectangles in a n x m grid

def rectCount(n, m):

	return (m * n * (n + 1) * (m + 1)) // 4

# Driver code
n, m = 5, 4
print(rectCount(n, m))

# This code is contributed by Anant Agarwal.
