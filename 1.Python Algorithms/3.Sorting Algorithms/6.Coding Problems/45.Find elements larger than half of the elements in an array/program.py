# Python program to find elements that are larger than
# half of the elements in array
# Prints elements larger than n/2 element
def findLarger(arr,n):

	# Sort the array in ascending order
	x = sorted(arr)

	# Print last ceil(n/2) elements
	for i in range(n/2,n):
		print(x[i]),

# Driver program
arr = [1, 3, 6, 1, 0, 9]
n = len(arr)
findLarger(arr,n)


