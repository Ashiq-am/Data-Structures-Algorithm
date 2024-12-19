# Python code Program to calculate volume and
# and surface area of a Hemisphere.
import math


# Function to calculate volume
def volume(r):
    volume = 2 * math.pi * math.pow(r, 3) / 3
    print("Volume = ", '%.4f' % volume)


# Function to calculate surface area
def surface_area(r):
    s_area = 2 * math.pi * math.pow(r, 2)
    print("Surface Area = ", '%.4f' % s_area)


# Driver code
r = 11
volume(r)
surface_area(r)
