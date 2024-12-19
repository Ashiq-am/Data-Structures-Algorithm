# Python Program to find minimum height of triangle
import math

def minHeight(area,base):
		return math.ceil((2*area)/base)

# Driver code
area = 8
base = 4
height = minHeight(area, base)
print("Minimum height is %d" % (height))
