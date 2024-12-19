# Python3 Program to
# Calculate area of
# tetrahedron
import math

def area_of_tetrahedron(side):
	return (math.sqrt(3) *
		(side * side))

# Driver Code
side = 3
print("Area of Tetrahedron = ", round(area_of_tetrahedron(side), 4))

# This code is contributed by mits
