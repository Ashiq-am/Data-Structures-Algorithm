# Python program to check whether
# the number is divisible by
# 8 or not using bitwise operator

import math

# function to check number is
# div by 8 or not using bitwise
# operator

def Div_by_8(n):

	return (((n >> 3) << 3) == n)


# driver code
n = 16
if (Div_by_8(n)):
	print("YES")
else:
	print("NO")

# This code is contributed by Gitanjali.
