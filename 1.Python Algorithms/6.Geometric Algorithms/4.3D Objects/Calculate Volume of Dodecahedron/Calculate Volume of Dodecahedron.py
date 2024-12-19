# Python3 program to calculate
# Volume of dodecahedron
import math


# utility Function
def vol_of_dodecahedron(side):
    return (((15 + (7 * (math.sqrt(5)))) / 4) * (math.pow(side, 3)))


# Driver Function
side = 4
print("Volume of dodecahedron =",round(vol_of_dodecahedron(side), 2))

# This code is contributed by Smitha Dinesh Semwal
