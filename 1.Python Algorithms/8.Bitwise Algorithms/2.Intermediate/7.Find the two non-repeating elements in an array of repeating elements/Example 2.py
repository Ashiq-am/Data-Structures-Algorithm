# Python program for Find the two
# non-repeating elements in an array
# of repeating elements/ Unique Numbers 2

# This function prints the two non-repeating elements in an
# array of repeating elements
def get2NonRepeatingNos(arr, n):

	# Create map and calculate frequency of array
	# elements
	m = {}
	for i in range(n):
		if(arr[i] not in m):
			m[arr[i]] = 0

		m[arr[i]] = m[arr[i]] + 1

	# Traverse through the map and check if its second
	# element that is the frequency is 1 or not. If this is
	# 1 than it is the non-repeating element print it.It is
	# clearly mentioned in problem that all numbers except
	# two are repeated once. So they will be printed
	print("The non-repeating elements are", end = " ")
	for key,value in m.items():
		if (value == 1):
			print(key,end = " ")

# Driver code
arr = [ 2, 3, 7, 9, 11, 2, 3, 11 ]
n = len(arr)
get2NonRepeatingNos(arr, n)

# This code is contributed by shinjanpatra
