# Python 3 program to count
# pairs in array whose XOR is odd

# A function will
# return number of pair
# whose XOR is odd
def countXorPair(arr, n):

	# To store count of XOR pair
	count = 0

	for i in range(n):
		for j in range(i + 1, n):

			# If XOR is odd increase count
			if ((arr[i] ^ arr[j]) % 2 == 1):
				count += 1

	# Return count
	return count

# Driver Code
if __name__ == "__main__":
	arr= [ 1, 2, 3 ]
	n = len(arr)
	print(countXorPair(arr, n))

# This code is contributed
# by ChitraNayal
