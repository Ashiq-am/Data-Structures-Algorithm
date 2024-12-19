# Python3 program to find
# count of values whose
# XOR with x is greater
# than x and values are
# smaller than x

def countValues(x):

	count = 0
	for i in range(1 ,x):
		if ((i ^ x) > x):
			count += 1
	return count

# Driver code
x = 10
print(countValues(x))

# This code is contributed
# by Smitha
