# Python3 Program to find kth element
# from two sorted arrays

def find(A, B, m, n, k_req):
	i, j, k = 0, 0, 0

	# Keep taking smaller of the current
	# elements of two sorted arrays and
	# keep incrementing k
	while i < len(A) and j < len(B):
		if A[i] < B[j]:
			k += 1
			if k == k_req:
				return A[i]
			i += 1
		else:
			k += 1
			if k == k_req:
				return B[i]
			j += 1

	# If array B[] is completely traversed
	while i < len(A):
		k += 1
		if k == k_req:
				return A[i]
		i += 1


	# If array A[] is completely traversed
	while j < len(B):
		k += 1
		if k == k_req:
				return B[j]
		j += 1

# driver code
A = [2, 3, 6, 7, 9]
B = [1, 4, 8, 10]
k = 5
print(find(A, B, 5, 4, k))
# time complexity of O(k)
