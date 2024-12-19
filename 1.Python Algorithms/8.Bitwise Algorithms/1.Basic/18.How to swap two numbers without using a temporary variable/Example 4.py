def swap(xp, yp):

	xp[0] = xp[0] ^ yp[0]
	yp[0] = xp[0] ^ yp[0]
	xp[0] = xp[0] ^ yp[0]


# Driver code
x = [10]
swap(x, x)
print("After swap(&x, &x): x = ", x[0])

# This code is contributed by SHUBHAMSINGH10
