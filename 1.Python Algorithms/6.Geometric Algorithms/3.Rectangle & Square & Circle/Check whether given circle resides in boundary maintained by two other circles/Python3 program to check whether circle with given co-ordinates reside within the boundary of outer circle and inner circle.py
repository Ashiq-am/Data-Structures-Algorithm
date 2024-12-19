# Python3 program to check
# whether circle with given
# co-ordinates reside
# within the boundary
# of outer circle
# and inner circle

import math


# function to check if
# given circle fit in
# boundary or not
def fitOrNotFit(R, r, x, y, rad):
    # Distance from the center
    val = math.sqrt(math.pow(x, 2) + math.pow(y, 2))

    # Checking the corners of circle
    if (val + rad <= R and val - rad >= R - r):
        print("Fits\n")
    else:
        print("Doesn't Fit")

    # driver program


# Radius of outer circle and inner circle
# respectively
R = 8
r = 4

# Co-ordinates and radius of the circle
# to be checked
x = 5
y = 3
rad = 3

fitOrNotFit(R, r, x, y, rad)

# This code is contributed by
# Smitha Dinesh Semwal
