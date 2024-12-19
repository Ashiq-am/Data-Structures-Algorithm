# Python program to check existence of
# right triangle.
from math import sqrt

# Prints three sides of a right trianlge
# from given area and hypotenuse if triangle
# is possible, else prints -1.
def findRightAngle(A, H):

	# Descriminant of the equation
	D = pow(H,4) - 16 * A * A
	if D >= 0:

		# applying the linear equation
		# formula to find both the roots
		root1 = (H * H + sqrt(D))/2
		root2 = (H * H - sqrt(D))/2

		a = sqrt(root1)
		b = sqrt(root2)
		if b >= a:
			print(a, b, H)
		else:
			print(b, a, H)
	else:
		print("-1")

# Driver code
# Area is 6 and hypotenuse is 5.
findRightAngle(6, 5)
