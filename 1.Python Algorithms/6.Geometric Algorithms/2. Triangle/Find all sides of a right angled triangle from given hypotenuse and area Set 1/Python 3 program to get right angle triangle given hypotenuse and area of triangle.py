# Python 3 program to get right angle triangle, given
# hypotenuse and area of triangle

# limit for float comparison
# define eps 1e-6
import math


# Utility method to get area of right angle triangle,
# given base and hypotenuse
def getArea(base, hypotenuse):
    height = math.sqrt(hypotenuse * hypotenuse - base * base)
    return 0.5 * base * height


# Prints base and height of triangle using hypotenuse
# and area information
def printRightAngleTriangle(hypotenuse, area):
    hsquare = hypotenuse * hypotenuse

    # maximum area will be obtained when base and height
    # are equal (= sqrt(h*h/2))
    sideForMaxArea = math.sqrt(hsquare / 2.0)
    maxArea = getArea(sideForMaxArea, hypotenuse)

    # if given area itself is larger than maxArea then no
    # solution is possible
    if (area > maxArea):
        print("Not possiblen")
        return

    low = 0.0
    high = sideForMaxArea

    # binary search for base
    while (abs(high - low) > 1e-6):
        base = (low + high) / 2.0
        if (getArea(base, hypotenuse) >= area):
            high = base
        else:
            low = base

        # get height by pythagorean rule
    height = math.ceil(math.sqrt(hsquare - base * base))
    base = math.floor(base)
    print(base, height)


# Driver code to test above methods
if __name__ == '__main__':
    hypotenuse = 5
    area = 6

    printRightAngleTriangle(hypotenuse, area)

# This code is contributed by
# Surendra_Gangwar
