# Python 3 program to find an
# extra element present in arr1[]


# Returns index of extra .
# element in arr1[] n is
# size of arr2[]. Size of
# arr1[] is n-1.
def findExtra(arr1, arr2, n) :
	for i in range(0, n) :
		if (arr1[i] != arr2[i]) :
			return i

	return n


# Driver code
arr1 = [2, 4, 6, 8, 10, 12, 13]
arr2 = [2, 4, 6, 8, 10, 12]
n = len(arr2)

# Solve is passed both arrays
print(findExtra(arr1, arr2, n))

# This code is contributed
# by Nikita Tiwari.
