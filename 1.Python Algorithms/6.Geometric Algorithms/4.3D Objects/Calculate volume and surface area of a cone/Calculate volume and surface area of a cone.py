''' Python3 program to calculate Volume and
	Surface area of Cone'''

# Importing Math library for value Of PI
import math
pi = math.pi

# Function to calculate Volume of Cone
def volume(r, h):
	return (1 / 3) * pi * r * r * h

# Function To Calculate Surface Area of Cone
def surfacearea(r, s):
	return pi * r * s + pi * r * r

# Driver Code
radius = float(5)
height = float(12)
slat_height = float(13)
print( "Volume Of Cone : ", volume(radius, height) )
print( "Surface Area Of Cone : ", surfacearea(radius, slat_height) )
