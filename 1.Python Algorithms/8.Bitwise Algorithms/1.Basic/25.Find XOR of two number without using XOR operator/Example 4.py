# Python3 program to return XOR of x and y without ^ operator
def XOR(x, y):
	return (x+y - (2*(x & y)))


# Driver Code
x = 3
y = 5
print("XOR of",x,'&',y,'is:',
	XOR(x, y))

# This code is contributed by vishu05
