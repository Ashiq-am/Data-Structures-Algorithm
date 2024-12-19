# Python3 code to calculate
# length of an arc
import math


# functuion to calculate arc length
def arcLength(diameter, angle):
    if angle >= 360:
        print("Angle cannot be formed")
        return 0
    else:
        arc = (3.142857142857143 * diameter) * (angle / 360.0)
        return arc

    # Driver Code


diameter = 25.0
angle = 45.0
arc_len = arcLength(diameter, angle)
print(arc_len)

# This code is contributed by "Sharad_Bhardwaj".
