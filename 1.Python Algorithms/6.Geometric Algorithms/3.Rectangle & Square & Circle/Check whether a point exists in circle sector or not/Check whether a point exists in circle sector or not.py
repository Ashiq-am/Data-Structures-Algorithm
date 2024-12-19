# Python3 program to check if a point
# lies inside a circle sector.
import math

def checkPoint(radius, x, y, percent, startAngle):

	# calculate endAngle
	endAngle = 360 / percent + startAngle

	# Calculate polar co-ordinates
	polarradius = math.sqrt(x * x + y * y)
	Angle = math.atan(y / x)

	# Check whether polarradius is less
	# then radius of circle or not and
	# Angle is between startAngle and
	# endAngle or not
	if (Angle >= startAngle and Angle <= endAngle
						and polarradius < radius):
		print("Point (", x, ",", y, ") "
			"exist in the circle sector")
	else:
		print("Point (", x, ",", y, ") "
			"does not exist in the circle sector")

# Driver code
radius, x, y = 8, 3, 4
percent, startAngle = 12, 0

checkPoint(radius, x, y, percent, startAngle)

# This code is contributed by
# Smitha Dinesh Semwal
