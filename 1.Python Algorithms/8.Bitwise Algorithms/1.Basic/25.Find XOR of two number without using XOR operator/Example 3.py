# Python3 program to
# Returns XOR of x and y
def myXOR(x, y):
	return (x & (~y)) | ((~x )& y)

# Driver Code
x = 3
y = 5
print("XOR is" ,
	myXOR(x, y))

# This code is contributed by shivanisinghss2110
