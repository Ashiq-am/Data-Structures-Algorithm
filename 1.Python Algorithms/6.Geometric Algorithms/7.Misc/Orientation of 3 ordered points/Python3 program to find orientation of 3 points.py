# A Python3 program to find orientation of 3 points
class Point:

    # to store the x and y coordinates of a point
    def __init__(self, x, y):
        self.x = x
        self.y = y


def orientation(p1, p2, p3):
    # to find the orientation of
    # an ordered triplet (p1,p2,p3)
    # function returns the following values:
    # 0 : Colinear points
    # 1 : Clockwise points
    # 2 : Counterclockwise
    val = (float(p2.y - p1.y) * (p3.x - p2.x)) - \
          (float(p2.x - p1.x) * (p3.y - p2.y))
    if (val > 0):

        # Clockwise orientation
        return 1
    elif (val < 0):

        # Counterclockwise orientation
        return 2
    else:

        # Colinear orientation
        return 0


# Driver code
p1 = Point(0, 0)
p2 = Point(4, 4)
p3 = Point(1, 2)

o = orientation(p1, p2, p3)

if (o == 0):
    print("Linear")
elif (o == 1):
    print("Clockwise")
else:
    print("CounterClockwise")


# This code is contributed by Ansh Riyal 
