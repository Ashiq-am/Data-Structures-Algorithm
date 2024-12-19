# Python3 program to find if a
# subarray is even or odd.

# Prints if subarray is even or odd
def checkEVENodd (arr, n, l, r):

	# if arr[r] = 1 print odd
	if (arr[r] == 1):
		print("odd")

	# if arr[r] = 0 print even
	else:
		print("even")

# Driver code
arr = [1, 1, 0, 1]
n = len(arr)
checkEVENodd (arr, n, 1, 3)

# This code is contributed by Anant Agarwal.
