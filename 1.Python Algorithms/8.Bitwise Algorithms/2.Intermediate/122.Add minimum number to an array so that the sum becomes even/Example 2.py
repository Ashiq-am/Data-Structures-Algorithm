# Python program to add minimum number
# so that the sum of array becomes even

# Function to find out minimum number
def minNum(arr, n):

	# Count odd number of terms in array
	odd = False
	for i in range(n):
		if (arr[i] % 2):
			odd = not odd
	if (odd):
		return 1
	return 2


# Driver code
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(arr)
print (minNum(arr, n))
