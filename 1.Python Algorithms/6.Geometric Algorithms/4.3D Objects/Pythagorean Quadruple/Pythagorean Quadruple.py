# Python code to detect
# Pythagorean Quadruples.
import math

# function for checking
def pythagorean_quadruple(a,b, c, d):

	sum = a * a + b * b + c * c
	if (d * d == sum):
		return True
	else:
		return False

#driver code
a = 1
b = 2
c = 2
d = 3
if (pythagorean_quadruple(a, b, c, d)):
	print("Yes")
else:
	print("No" )

# This code is contributed
# by Gitanjali.
