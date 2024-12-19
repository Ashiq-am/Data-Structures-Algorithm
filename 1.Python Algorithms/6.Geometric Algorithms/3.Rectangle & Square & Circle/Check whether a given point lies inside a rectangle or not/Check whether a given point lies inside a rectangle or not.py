# A utility function to calculate
# area of triangle formed by (x1, y1),
# (x2, y2) and (x3, y3)
def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) +
                x2 * (y3 - y1) +
                x3 * (y1 - y2)) / 2.0)


# A function to check whether point
# P(x, y) lies inside the rectangle
# formed by A(x1, y1), B(x2, y2),
# C(x3, y3) and D(x4, y4)
def check(x1, y1, x2, y2, x3,
          y3, x4, y4, x, y):
    # Calculate area of rectangle ABCD
    A = (area(x1, y1, x2, y2, x3, y3) +
         area(x1, y1, x4, y4, x3, y3))

    # Calculate area of triangle PAB
    A1 = area(x, y, x1, y1, x2, y2)

    # Calculate area of triangle PBC
    A2 = area(x, y, x2, y2, x3, y3)

    # Calculate area of triangle PCD
    A3 = area(x, y, x3, y3, x4, y4)

    # Calculate area of triangle PAD
    A4 = area(x, y, x1, y1, x4, y4);

    # Check if sum of A1, A2, A3
    # and A4 is same as A
    return (A == A1 + A2 + A3 + A4)


# Driver Code
if __name__ == '__main__':

    # Let us check whether the point
    # P(10, 15) lies inside the
    # rectangle formed by A(0, 10),
    # B(10, 0) C(0, -10) D(-10, 0)
    if (check(0, 10, 10, 0, 0, -10,
              -10, 0, 10, 15)):
        print("yes")
    else:
        print("no")

    # This code is contributed by
# Surendra_Gangwar
