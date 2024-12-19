# Python3 Program to find maximum XOR
# value of a pair

# Utility function to check number of
# elements having set msb as of pattern


def checkBit(pattern, arr, n):
	count = 0

	for i in range(0, n):
		if ((pattern & arr[i]) == pattern):
			count = count + 1
	return count

# Function for finding maximum and
# value pair


def maxAND(arr, n):
	res = 0

	# iterate over total of 32bits
	# from msb to lsb
	for bit in range(31, -1, -1):

		# find the count of element
		# having set msb
		count = checkBit(res | (1 << bit), arr, n)

		# if count >= 2 set particular
		# bit in result
		if (count >= 2):
			res = res | (1 << bit)

	return res


# Driver function
arr = [4, 8, 6, 2]
n = len(arr)
print("Maximum AND Value = ", maxAND(arr, n))

# This code is contributed by Nikita Tiwari
