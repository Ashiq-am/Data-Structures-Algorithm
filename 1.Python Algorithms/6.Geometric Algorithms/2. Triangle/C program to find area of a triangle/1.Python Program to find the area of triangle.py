# Python Program to find the area
# of triangle

# Length of sides must be positive
# and sum of any two sides
def findArea(a, b, c):
    # must be smaller than third side.
    if (a < 0 or b < 0 or c < 0 or (a + b <= c) or (a + c <= b) or (b + c <= a)):
        print('Not a valid trianglen')
        return

    # calculate the semi-perimeter
    s = (a + b + c) / 2

    # calculate the area
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print('Area of a traingle is %f' % area)


# Initialize first side of traingle
a = 3.0
# Initialize second side of traingle
b = 4.0
# Initialize Third side of traingle
c = 5.0
findArea(a, b, c)

# This code is contributed by Shariq Raza
# Python Program to find the area
# of triangle

# Length of sides must be positive
# and sum of any two sides
def findArea(a, b, c):
    # must be smaller than third side.
    if (a < 0 or b < 0 or c < 0 or (a + b <= c) or (a + c <= b) or (b + c <= a)):
        print('Not a valid trianglen')
        return

    # calculate the semi-perimeter
    s = (a + b + c) / 2

    # calculate the area
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print('Area of a traingle is %f' % area)


# Initialize first side of traingle
a = 3.0
# Initialize second side of traingle
b = 4.0
# Initialize Third side of traingle
c = 5.0
findArea(a, b, c)
