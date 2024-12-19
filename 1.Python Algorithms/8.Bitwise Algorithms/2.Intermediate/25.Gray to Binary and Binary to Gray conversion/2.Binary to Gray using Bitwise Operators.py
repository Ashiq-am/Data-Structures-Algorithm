# Python3 code for above approach
def greyConverter(n):

	return n ^ (n >> 1)


n = 3
print(greyConverter(n))

n = 9
print(greyConverter(n))

# This code is contributed by divyeshrabadiya07
