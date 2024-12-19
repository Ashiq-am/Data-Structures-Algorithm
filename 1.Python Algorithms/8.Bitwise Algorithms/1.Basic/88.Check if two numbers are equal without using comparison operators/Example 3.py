# Python code to check if 2 numbers are same

# Finds if a and b are same
def areSame(a, b):
	if (a & ~b):
		print ("Not Same")
	else:
		print ("Same")
# Driver code
areSame(10, 10)
areSame(10, 20)

# This code is contributed by phasing17
