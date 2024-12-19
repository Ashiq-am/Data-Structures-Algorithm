# Python Program to calculate
# surface area of Octahedron.
import math

# utility Function
def surface_area_octahedron( side):

	return (2*(math.sqrt(3))*(side*side))

# driver code
side = 7
print("Surface area of octahedron =" ,
	surface_area_octahedron(side))

# This code is contributed by Gitanjali.
