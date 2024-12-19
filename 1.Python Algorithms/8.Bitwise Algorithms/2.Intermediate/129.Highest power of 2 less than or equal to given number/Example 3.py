# Python3 program to find highest
# power of 2 smaller than or
# equal to n.
import math

def highestPowerof2(n):

	p = int(math.log(n, 2))
	return int(pow(2, p))

# Driver code
n = 10
print(highestPowerof2(n))

# This code is contributed by mits
