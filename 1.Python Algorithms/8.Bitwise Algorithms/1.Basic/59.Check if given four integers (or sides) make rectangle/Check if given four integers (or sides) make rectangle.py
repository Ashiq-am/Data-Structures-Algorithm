# A simple program to find if given 4
# values can represent 4 sides of rectangle

# Function to check if the given
# integers value make a rectangle


def isRectangle(a, b, c, d):

	# check all sides of rectangle combinations
	if (a == b and d == c) or (a == c and b == d) or (a == d and b == c):
		return True
	else:
		return False


# Driver code
a, b, c, d = 1, 2, 3, 4
print("Yes" if isRectangle(a, b, c, d) else "No")


# This code is contributed by Jatinder SIngh
