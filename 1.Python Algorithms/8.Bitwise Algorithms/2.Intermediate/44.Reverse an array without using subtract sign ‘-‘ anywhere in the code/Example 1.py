# Python program to reverse an array without
# using "-" sign

# Function to reverse array
def reverseArray(arr, n):

	import sys

	# Trick to assign - 1 to a variable
	x = -sys.maxsize // sys.maxsize

	# Reverse array in simple manner
	for i in range(n//2):

		# Swap ith index value with (n-i-1)th
		# index value
		arr[i], arr[n + (x*i) + x] = arr[n + (x*i) + x], arr[i]


# Driver code
if __name__ == "__main__":
	arr = [5, 3, 7, 2, 1, 6]
	n = len(arr)

	reverseArray(arr, n)

	# print the reversed array
	for i in range(n):
		print(arr[i], end=" ")

# This code is contributed by
# sanjeev2552
