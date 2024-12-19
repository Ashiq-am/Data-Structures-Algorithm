# Python3 Find the sum of all
# non- repeated elements in an array

# Find the sum of all non-repeated
# elements in an array
def findSum(arr, n):
	s = set()
	sum = 0

	# Hash to store all element
	# of array
	for i in range(n):
		if arr[i] not in s:
			s.add(arr[i])
	for i in s:
		sum = sum + i

	return sum

# Driver code
arr = [1, 2, 3, 1, 1, 4, 5, 6]
n = len(arr)
print(findSum(arr, n))
