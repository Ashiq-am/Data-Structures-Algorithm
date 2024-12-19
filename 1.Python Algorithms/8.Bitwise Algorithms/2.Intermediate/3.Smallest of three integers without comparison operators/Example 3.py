# Using division operator to find
# minimum of three numbers
def smallest(x, y, z):

	if (not (y / x)): # Same as "if (y < x)"
		return y if (not (y / z)) else z
	return x if (not (x / z)) else z

# Driver Code
if __name__== "__main__":

	x = 78
	y = 88
	z = 68
	print("Minimum of 3 numbers is", smallest(x, y, z))

# This code is contributed
# by ChitraNayal
