# Python3 program to
# find area of octagon

import math

# Utility function
def areaOctagon(side):
	return (2 * (1 + (math.sqrt(2))) * side * side)

# Driver function
side = 4
print("Area of Regular Octagon =",round(areaOctagon(side), 4))
