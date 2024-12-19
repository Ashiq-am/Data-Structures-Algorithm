# Python program to find
# smallest power of 2
# greater than or equal to n
#include <iostream>
def nextPowerOf2(N):
	# if N is a power of two simply return it
	if not (N & (N - 1)):
		return N
	# else set only the left bit of most significant bit
	return int("1" + (len(bin(N)) - 2) * "0", 2)

# Driver Code
n = 5
print(nextPowerOf2(n))

# this code is contributed by phasing17
