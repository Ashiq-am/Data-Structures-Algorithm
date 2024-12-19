# Python3 program to find minimum area of
# polygon of number of sides more than three
# with given three points.

# from math lib import every function
from math import *

# assigning pi value to variable
pi = 3.14159265359

# calculating gcd value of two double values .
def gcd(x, y) :

	if abs(y) < 1e-4 :
		return x
	else :
		return gcd(y, fmod(x, y))


# Calculating minimum area of polygon
# through this function .
def min_area_of_polygon(Ax, Ay, Bx,
						By, Cx, Cy) :

	# calculating the length of the sides of
	# the triangle formed from given points
	# a, b, c represents the length of different
	# sides of triangle
	a = sqrt((Bx - Cx) * (Bx - Cx) +
			(By - Cy) * (By - Cy))
	b = sqrt((Ax - Cx) * (Ax - Cx) +
			(Ay - Cy) * (Ay - Cy))
	c = sqrt((Ax - Bx) * (Ax - Bx) +
			(Ay - By) * (Ay - By))

	# here we have calculated the semiperimeter
	# of a triangle .
	semiperimeter = (a + b + c) / 2

	# Now from the semiperimeter area of triangle
	# is derived through the heron's formula
	area_triangle = sqrt(semiperimeter *
						(semiperimeter - a) *
						(semiperimeter - b) *
						(semiperimeter - c))

	# thus circumradius of the triangle is derived
	# from the sides and area of the triangle calculated
	Radius = (a * b * c) / (4 * area_triangle)

	# Now each angle of the triangle is derived
	# from the sides of the triangle
	Angle_A = acos((b * b + c * c - a * a) / (2 * b * c))
	Angle_B = acos((a * a + c * c - b * b) / (2 * a * c))
	Angle_C = acos((b * b + a * a - c * c) / (2 * b * a))

	# Now n is calculated such that area is
	# minimum for the regular n-gon
	n = pi / gcd(gcd(Angle_A, Angle_B), Angle_C)

	# calculating area of regular n-gon through
	# the circumradius of the triangle
	area = (n * Radius * Radius *
			sin((2 * pi) / n)) / 2

	return area

# Driver Code
if __name__ == "__main__" :

	# three points are given as input .
	Ax = 0.00
	Ay = 0.00
	Bx = 1.00
	By = 1.00
	Cx = 0.00
	Cy = 1.00

	print(round(min_area_of_polygon(Ax, Ay, Bx, By, Cx, Cy), 1))


