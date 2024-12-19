# Python3 Program
# to find area of
# segment of a
# circle
import math

pi = 3.14159


# Function to find
# area of segment
def area_of_segment(radius, angle):

    # Calculating area of sector
    area_of_sector = pi * (radius * radius) *(angle / 360)

    # Calculating area of triangle
    area_of_triangle = 1 / 2 * (radius * radius) * math.sin((angle * pi) / 180)
    return area_of_sector - area_of_triangle

# Driver Code
radius = 10.0
angle = 90.0
print("Area of minor segment =",
      area_of_segment(radius, angle))
print("Area of major segment =",
      area_of_segment(radius, (360 - angle)))

# This code is contributed by Smitha Dinesh Semwal
