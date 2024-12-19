# Python program to Sort square
# of the numbers of the array

# Function to sort an square array
def sortSquare(arr, n):

	# First convert each array
	# elements into its square
	for i in range(n):
		arr[i]= arr[i] * arr[i]
	arr.sort()

# Driver code
arr = [-6, -3, -1, 2, 4, 5]
n = len(arr)

print("Before sort")
for i in range(n):
	print(arr[i], end = " ")

print("\n")

sortSquare(arr, n)

print("After sort")
for i in range(n):
	print(arr[i], end = " ")


