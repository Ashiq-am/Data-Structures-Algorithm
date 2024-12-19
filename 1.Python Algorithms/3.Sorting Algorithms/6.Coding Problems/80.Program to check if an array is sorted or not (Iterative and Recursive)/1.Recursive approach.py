# Recursive approach to check if an
# Array is sorted or not

# Function that returns 0 if a pair
# is found unsorted


def arraySortedOrNot(arr):

	# Calculating length
	n = len(arr)

	# Array has one or no element or the
	# rest are already checked and approved.
	if n == 1 or n == 0:
		return True

	# Recursion applied till last element
	return arr[0] <= arr[1] and arraySortedOrNot(arr[1:])


arr = [20, 23, 23, 45, 78, 88]

# Displaying result
if arraySortedOrNot(arr):
	print("Yes")
else:
	print("No")
