# Python3 program to find third side
# of triangle using law of cosines
import math as mt

# Function to calculate cos
# value of angle c
def cal_cos(n):

	accuracy = 0.0001
	x1, denominator, cosx, cosval = 0, 0, 0, 0

	# Converting degrees to radian
	n = n * (3.142 / 180.0)

	x1 = 1

	# Maps the sum along the series
	cosx = x1

	# Holds the actual value of sin(n)
	cosval = mt.cos(n)
	i = 1
	while (accuracy <= abs(cosval - cosx)):

		denominator = 2 * i * (2 * i - 1)
		x1 = -x1 * n * n / denominator
		cosx = cosx + x1
		i = i + 1

	return cosx

# Function to find third side
def third_side(a, b, c):
	angle = cal_cos(c)
	return mt.sqrt((a * a) +
				(b * b) - 2 * a * b * angle)

# Driver Code
c = 49
a, b = 5, 8
print(third_side(a, b, c))

# This code is contributed by mohit kumar
