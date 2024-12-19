# Python 3 Program to find
# magic index.

def magicIndex(arr, start, end):

	# If No Magic Index return -1
	if (start > end):
		return -1

	midIndex = int((start + end) / 2)
	midValue = arr[midIndex]

	# Magic Index Found, return it.
	if (midIndex == midValue):
		return midIndex

	# Search on Left side
	left = magicIndex(arr, start, min(midValue,
								midIndex - 1))

	# If Found on left side, return.
	if (left >= 0):
		return left

	# Return ans from right side.
	return magicIndex(arr, max(midValue,
						midIndex + 1),
									end)

# Driver program
arr = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
n = len(arr)

index = magicIndex(arr, 0, n - 1)

if (index == -1):
	print("No Magic Index")
else:
	print("Magic Index is :", index)

# This code is contributed by Smitha Dinesh Semwal
