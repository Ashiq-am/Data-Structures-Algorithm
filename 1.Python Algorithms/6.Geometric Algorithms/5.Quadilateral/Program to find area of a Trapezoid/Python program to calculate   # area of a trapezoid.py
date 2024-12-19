# Python program to calculate
# area of a trapezoid

# Function for the area
def Area(b1, b2, h):
	return ((b1 + b2) / 2) * h

# Driver Code
base1 = 8; base2 = 10; height = 6
area = Area(base1, base2, height)
print("Area is:", area)
