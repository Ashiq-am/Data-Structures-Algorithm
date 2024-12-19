# Python3 code to calculate
# Volume and Surface area of
# frustum of cone
import math

pi = math.pi


# Function to calculate Volume
# of frustum of cone
def volume(r, R, h):
    return 1 / 3 * pi * h * (r * r + R * R + r * R)


# Function to calculate Curved
# Surface area of frustum of cone
def curved_surface_area(r, R, l):
    return pi * l * (R + r)


# Function to calculate Total
# Surface area of frustum of cone
def total_surface_area(r, R, l, h):
    return pi * l * (R + r) + pi * (r * r + R * R)


# Driver Code
small_radius = 3
big_radius = 8
slant_height = 13
height = 12

# Printing value of volume
# and surface area
print("Volume Of Frustum of Cone : ", end='')
print(volume(small_radius, big_radius,height))

print("Curved Surface Area Of Frustum" + " of Cone : ", end='')
print(curved_surface_area(small_radius,big_radius, slant_height))

print("Total Surface Area Of Frustum" + " of Cone : ", end='')
print(total_surface_area(small_radius,big_radius, slant_height, height))

