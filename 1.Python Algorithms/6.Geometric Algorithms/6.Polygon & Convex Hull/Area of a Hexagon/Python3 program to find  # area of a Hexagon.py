# Python3 program to find
# area of a Hexagon
import math


# Function for calculating
# area of the hexagon.
def hexagonArea(s):
    return ((3 * math.sqrt(3) *
             (s * s)) / 2)


# Driver code
if __name__ == "__main__":
    # length of a side.
    s = 4

    print("Area:", "{0:.4f}".format(hexagonArea(s)))
