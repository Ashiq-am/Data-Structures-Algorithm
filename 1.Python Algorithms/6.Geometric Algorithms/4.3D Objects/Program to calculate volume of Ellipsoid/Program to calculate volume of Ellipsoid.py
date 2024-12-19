''' Python3 program to Volume of ellipsoid'''
import math

# Function To calculate Volume
def volumeOfEllipsoid(r1, r2, r3):
	return 1.33 * math.pi * r1 * r2 * r3


# Driver Code
r1 = float(2.3)
r2 = float(3.4)
r3 = float(5.7)
print( "Volume of ellipsoid is : ",
		volumeOfEllipsoid(r1, r2, r3) )
