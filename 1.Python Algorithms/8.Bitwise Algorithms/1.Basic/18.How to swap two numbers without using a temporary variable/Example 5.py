# Python3 program of above approach
def swap(xp, yp):

	# Check if the two addresses are same
	if (xp[0] == yp[0]):
		return
	xp[0] = xp[0] + yp[0]
	yp[0] = xp[0] - yp[0]
	xp[0] = xp[0] - yp[0]


# Driver Code
x = [10]
swap(x, x)
print("After swap(&x, &x): x = ", x[0])

# This code is contributed by SHUBHAMSINGH10
