# Python program to find whether a given number is a power of 4 or not.

import math


# Function to check if x is power of 4
def isPowerOfFour(n):
	if (n != 0 and n == pow(4, (math.log(n)/math.log(4)))):
		return True
	return False


test_no = 64
if(isPowerOfFour(test_no)):
	print(test_no, ' is a power of 4')
else:
	print(test_no, ' is not a power of 4')


# This code is contributed by lokesh (lokeshmvs21).
