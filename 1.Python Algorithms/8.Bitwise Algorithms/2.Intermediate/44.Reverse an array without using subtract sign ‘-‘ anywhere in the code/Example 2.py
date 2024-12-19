# Python program to reverse an array without
# using "-" sign

# Function to reverse array
def reverseArray(arr, n):

	# Reverse array in simple manner
	for i in range(n//2):

		# Swap ith index value with (n-i-1)th
		# index value
		# Note : A - B = A + ~B + 1
		# So n - i = n + ~i + 1 then
		# n - i - 1 = (n + ~i + 1) + ~1 + 1
		arr[i], arr[(n + ~i + 1) + ~1 + 1] = arr[(n + ~i + 1) + ~1 + 1],arr[i]

# Driver code

arr = [ 5, 3, 7, 2, 1, 6 ]
n = len(arr)

reverseArray(arr, n)

# print the reversed array
for i in range(n):
	print(arr[i],end=" ")

# This code is contributed by ankush_953
