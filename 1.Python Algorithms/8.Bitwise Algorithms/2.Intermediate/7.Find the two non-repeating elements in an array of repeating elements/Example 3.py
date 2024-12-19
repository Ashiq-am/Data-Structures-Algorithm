# Python3 code to find 2 non repeating elements
# in array that has pairs of numbers

# Method to print the 2 non repeating
# elements in an array
def print2SingleNumbers(nums):

	# Create a set to store the numbers
	set_ = set()

	n = len(nums)

	# Iterate through the array and check if each
	# element is present or not in the set. If the
	# element is present, remove it from the array
	# otherwise add it to the set

	for i in nums:
		if i in set_:
			set_.remove(i)
		else:
			set_.add(i)

	# Since there will only be 2 non
	# repeating elements we can
	# directly print them
	print("The 2 non repeating numbers are : " + " ".join(map(str, set_)))

# Driver Code
nums = [2, 3, 7, 9, 11, 2, 3, 11]

# Function Call
print2SingleNumbers(nums)

# This code is contributed by phasing17
