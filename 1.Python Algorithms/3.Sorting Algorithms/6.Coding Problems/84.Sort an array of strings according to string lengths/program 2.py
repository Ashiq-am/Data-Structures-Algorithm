# Python code for the above approach
def printsorted(arr):

	# Sorting using sorted function
	# providing key as len
	print(*sorted(arr, key=len))


# Driver code
arr = ["GeeksforGeeks", "I", "from", "am"]

# Passing list to printsorted function
printsorted(arr)
