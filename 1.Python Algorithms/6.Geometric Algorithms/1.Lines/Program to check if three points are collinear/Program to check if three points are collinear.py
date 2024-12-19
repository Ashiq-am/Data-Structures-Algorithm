# Python program to check
# if three points are collinear
# or not using area of triangle.

# function to check if
# point collinear or not
def collinear(x1, y1, x2, y2, x3, y3):
    """ Calculation the area of
        triangle. We have skipped
        multiplication with 0.5 to
        avoid floating point computations """
    a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)

    if (a == 0):
        print("Yes")
    else:
        print("No")


# Driver Code
x1, x2, x3, y1, y2, y3 = 1, 1, 1, 1, 4, 5
collinear(x1, y1, x2, y2, x3, y3)
