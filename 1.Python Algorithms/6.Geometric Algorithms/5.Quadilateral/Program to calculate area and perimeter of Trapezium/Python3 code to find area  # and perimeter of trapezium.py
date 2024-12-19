# Python3 code to find area
# and perimeter of trapezium

# Function to calculate
# Area of trapezium
def areaTrapezium (a, b, h):
	return (1.0 / 2 * (a + b) * h)

# Function to calculate
# perimeter of trapezium
def perimeterTrapezium (a, b, c, d):
	return (a + b + c + d)

# Driver function
a = 5
b = 15
c = 11
d = 4
h = 20
print("Area of Trapezium =",
	areaTrapezium(a, b, h))

print("Perimeter of Trapezium =",
	perimeterTrapezium(a, b, c, d))
