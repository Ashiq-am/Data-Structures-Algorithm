# Python3 program to determine direction
# of point from line segment

# Structure for point in cartesian plane.
class point:

    def __init__(self):
        self.x = 0
        self.y = 0


# Constant integers for directions
RIGHT = 1
LEFT = -1
ZERO = 0


def directionOfPoint(A, B, P):
    global RIGHT, LEFT, ZERO

    # Subtracting co-ordinates of
    # point A from B and P, to
    # make A as origin
    B.x -= A.x
    B.y -= A.y
    P.x -= A.x
    P.y -= A.y

    # Determining cross Product
    cross_product = B.x * P.y - B.y * P.x

    # Return RIGHT if cross product is positive
    if (cross_product > 0):
        return RIGHT

    # Return LEFT if cross product is negative
    if (cross_product < 0):
        return LEFT

    # Return ZERO if cross product is zero
    return ZERO


# Driver code
if __name__ == "__main__":

    A = point()
    B = point()
    P = point()

    A.x = -30
    A.y = 10  # A(-30, 10)
    B.x = 29
    B.y = -15  # B(29, -15)
    P.x = 15
    P.y = 28  # P(15, 28)

    direction = directionOfPoint(A, B, P)

    if (direction == 1):
        print("Right Direction")
    elif (direction == -1):
        print("Left Direction")
    else:
        print("Point is on the Line")

# This code is contributed by rutvik_56
