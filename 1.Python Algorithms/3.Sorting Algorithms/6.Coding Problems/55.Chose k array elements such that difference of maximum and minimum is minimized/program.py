# Python program to find minimum
# difference of maximum
# and minimum of K number.

# Return minimum difference
# of maximum and minimum
# of k elements of arr[0..n-1].
def minDiff(arr,n,k):
	result = +2147483647

	# Sorting the array.
	arr.sort()

	# Find minimum value among
	# all K size subarray.
	for i in range(n-k+1):
		result = int(min(result, arr[i+k-1] - arr[i]))

	return result

# Driver code

arr= [10, 100, 300, 200, 1000, 20, 30]
n =len(arr)
k = 3

print(minDiff(arr, n, k))