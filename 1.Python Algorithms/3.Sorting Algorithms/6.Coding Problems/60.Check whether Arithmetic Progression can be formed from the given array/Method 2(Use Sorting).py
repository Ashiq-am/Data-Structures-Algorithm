# Python3 program to check if a given
# array can form arithmetic progression

# Returns true if a permutation of arr[0..n-1]
# can form arithmetic progression
def checkIsAP(arr, n):
	if (n == 1): return True

	# Sort array
	arr.sort()

	# After sorting, difference between
	# consecutive elements must be same.
	d = arr[1] - arr[0]
	for i in range(2, n):
		if (arr[i] - arr[i-1] != d):
			return False

	return True

# Driver code
arr = [ 20, 15, 5, 0, 10 ]
n = len(arr)
print("Yes") if(checkIsAP(arr, n)) else print("No")
