# Python3 program to calculate Area and
# Perimeter of equilateral Triangle

# Importing Math library for sqrt
from math import *


# Function to calculate Area
# of equilateral triangle
def area_equilateral(side):
    area = (sqrt(3) / 4) * side * side
    print("Area of Equilateral Triangle: % f" % area)


# Function to calculate Perimeter
# of equilateral triangle
def perimeter(side):
    perimeter = 3 * side
    print("Perimeter of Equilateral Triangle: % f" % perimeter)


# Driver code
side = 4
area_equilateral(side)
perimeter(side)
