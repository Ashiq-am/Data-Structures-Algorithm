# Python3 code to implement an interesting XOR
# based method to check if a number is multiple of 4.

# Returns true if n is a multiple of 4.
def isMultipleOf4(n):
	if (n == 0):
		return True

	return (((n>>2)<<2) == n)

# Driver code to print multiples of 4
#Printing multiples of 4 using above method
for n in range(43):
	if isMultipleOf4(n):
		print(n, end = " ")

# This codeis contributed by phasing17
