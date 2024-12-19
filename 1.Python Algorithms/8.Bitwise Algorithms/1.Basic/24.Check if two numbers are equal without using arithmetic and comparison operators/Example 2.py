# Python3 program to check if two numbers
# are equal without using arithmetic
# and comparison operators

# Function to check if two
# numbers are equal using
# using ~ complement and & operator.


def areSame(a, b):
	if ((a & ~b) == 0 and (~a & b) == 0):
		print("Same")
	else:
		print("Not Same")


# Calling function
areSame(10, 20)

# This code is contributed by Rajput-Ji
