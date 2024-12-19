# Python3 program to swap two numbers

# Function to swap the numbers


def swap(a, b):

	# Same as a = a + b
	a = (a & b) + (a | b)

	# Same as b = a - b
	b = a + (~b) + 1

	# Same as a = a - b
	a = a + (~b) + 1

	print("After Swapping: a = ", a, ", b = ", b)


# Driver code
a = 5
b = 10

# Function call
swap(a, b)

# This code is contributed by bunnyram19
