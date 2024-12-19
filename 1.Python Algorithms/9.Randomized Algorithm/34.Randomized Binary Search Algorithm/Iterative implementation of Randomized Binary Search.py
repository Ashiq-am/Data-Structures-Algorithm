# Python program to implement iterative
# randomized algorithm.

# To generate random number
# between x and y ie.. [x, y]

from random import randint

def getRandom(x, y):
	return randint(x,y)

# A iterative randomized binary search function.
# It returns location of x in
# given array arr[l..r] if present, otherwise -1
def randomizedBinarySearch(arr, l, r, x):
	while (l <= r):
		# Here we have defined middle as
		# random index between l and r ie.. [l, r]
		m = getRandom(l, r)

		# Check if x is present at mid
		if (arr[m] == x):
			return m

		# If x greater, ignore left half
		if (arr[m] < x):
			l = m + 1

		# If x is smaller, ignore right half
		else:
			r = m - 1
	# if we reach here, then element was
	# not present
	return -1

# Driver code
arr = [2, 3, 4, 10, 40]
n = len(arr)
x = 10
result = randomizedBinarySearch(arr, 0, n-1, x)
if result == 1:
	print("Element is not present in array")
else:
	print("Element is present at index", result)
