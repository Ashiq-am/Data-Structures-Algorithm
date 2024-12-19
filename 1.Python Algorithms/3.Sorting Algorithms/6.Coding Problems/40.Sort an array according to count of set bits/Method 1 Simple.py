# Python 3 program to implement simple approach to sort
# an array according to count of set bits.

# a utility function that returns total set bits
# count in an integer
def countBits(a):
	count = 0
	while (a):
		if (a & 1):
			count+= 1
		a = a>>1

	return count

# Function to simultaneously sort both arrays
# using insertion sort
# ( http:#quiz.geeksforgeeks.org/insertion-sort/ )
def insertionSort(arr,aux, n):
	for i in range(1,n,1):
		# use 2 keys because we need to sort both
		# arrays simultaneously
		key1 = aux[i]
		key2 = arr[i]
		j = i-1

		# Move elements of arr[0..i-1] and aux[0..i-1],
		# such that elements of aux[0..i-1] are
		# greater than key1, to one position ahead
		# of their current position */
		while (j >= 0 and aux[j] < key1):
			aux[j+1] = aux[j]
			arr[j+1] = arr[j]
			j = j-1

		aux[j+1] = key1
		arr[j+1] = key2

# Function to sort according to bit count using
# an auxiliary array
def sortBySetBitCount(arr, n):
	# Create an array and store count of
	# set bits in it.
	aux = [0 for i in range(n)]
	for i in range(0,n,1):
		aux[i] = countBits(arr[i])

	# Sort arr[] according to values in aux[]
	insertionSort(arr, aux, n)

# Utility function to print an array
def printArr(arr, n):
	for i in range(0,n,1):
		print(arr[i],end = " ")

# Driver Code
if __name__ =='__main__':
	arr = [1, 2, 3, 4, 5, 6]
	n = len(arr)
	sortBySetBitCount(arr, n)
	printArr(arr, n)
