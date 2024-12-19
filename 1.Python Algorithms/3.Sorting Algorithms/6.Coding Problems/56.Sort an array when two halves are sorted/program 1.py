# Python program to Merge two sorted
# halves of array Into Single Sorted Array


def mergeTwoHalf(A, n):

	# Sort the given array using sort STL
	A.sort()


# Driver Code
if __name__ == '__main__':
	A = [2, 3, 8, -1, 7, 10]
	n = len(A)
	mergeTwoHalf(A, n)

	# Print sorted Array
	for i in range(n):
		print(A[i], end=" ")
