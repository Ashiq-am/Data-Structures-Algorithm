# Program to find smallest rectangle
# to conquer all points

# function to print coordinate of smallest rectangle
def printRect(X, Y, n):

	# find Xmax and Xmin
	Xmax = max(X)
	Xmin = min(X)

	# find Ymax and Ymin
	Ymax = max(Y)
	Ymin = min(Y)

	# print all four coordinates
	print("{",Xmin,", ",Ymin,"}",sep="" )
	print("{",Xmin,", ",Ymax,"}",sep="" )
	print("{",Xmax,", ",Ymax,"}",sep="" )
	print("{",Xmax,", ",Ymin,"}",sep="" )

# driver program
X = [4, 3, 6, 1, -1, 12]
Y = [4, 1, 10, 3, 7, -1]
n = len(X)
printRect(X, Y, n)
# This code is contributed by
# Smitha Dinesh Semwal
