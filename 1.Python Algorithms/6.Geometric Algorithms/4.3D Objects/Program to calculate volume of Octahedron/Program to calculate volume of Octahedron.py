# Python3 Program to calculate
# volume of Octahedron

import math

# utility Function
def vol_of_octahedron(side):
	return ((side*side*side)*(math.sqrt(2)/3))

# Driver Function
side = 3
print("Volume of octahedron =", round(vol_of_octahedron(side),4))

# This code is contributed
# by Azkia Anam.
