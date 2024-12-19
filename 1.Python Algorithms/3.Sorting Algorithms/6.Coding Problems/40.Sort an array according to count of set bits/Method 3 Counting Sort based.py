# Python3 program to sort an array according to
# count of set bits using std::sort()

# a utility function that returns total set bits
# count in an integer
def countBits(a):
	count = 0
	while (a):
		if (a & 1 ):
			count += 1
		a = a>>1
	return count

# Function to sort according to bit count
# This function assumes that there are 32
# bits in an integer.
def sortBySetBitCount(arr,n):
	count = [[] for i in range(32)]
	setbitcount = 0
	for i in range(n):
		setbitcount = countBits(arr[i])
		count[setbitcount].append(arr[i])

	j = 0 # Used as an index in final sorted array

	# Traverse through all bit counts (Note that we
	# sort array in decreasing order)
	for i in range(31, -1, -1):
		v1 = count[i]
		for i in range(len(v1)):
			arr[j] = v1[i]
			j += 1

# Utility function to pran array
def printArr(arr, n):
	print(*arr)

# Driver Code
arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
sortBySetBitCount(arr, n)
printArr(arr, n)
