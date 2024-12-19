# Python 3 code to find mirror image

# Python function which finds coordinates
# of mirror image.
# This function return a pair of double
def mirrorImage( a, b, c, x1, y1):
	temp = -2 * (a * x1 + b * y1 + c) /(a * a + b * b)
	x = temp * a + x1
	y = temp * b + y1
	return (x, y)

# Driver code to test above function
a = -1.0
b = 1.0
c = 0.0
x1 = 1.0
y1 = 0.0

x, y = mirrorImage(a, b, c, x1, y1);
print("Image of point (" + str (x1) + ", " + str( y1) + ") ")
print("by mirror (" + str (a) + ")x + (" + str( b) + ")y + (" +str(c) + ") = 0, is :")
print( "(" + str(x) + ", " + str(y) + ")" )

# This code is contributed by ApurvaRaj
