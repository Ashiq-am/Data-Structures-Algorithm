# Python3 Program to find maximum XOR
# value of a pair

# Function for finding maximum and value pair


def maxAND(arr, n):
	res = 0

	for i in range(0, n):
		for j in range(i + 1, n):
			res = max(res, arr[i] & arr[j])

	return res


# Driver function
arr = [4, 8, 6, 2]
n = len(arr)
print("Maximum AND Value = ", maxAND(arr, n))

# This code is contributed by Nikita Tiwari.
