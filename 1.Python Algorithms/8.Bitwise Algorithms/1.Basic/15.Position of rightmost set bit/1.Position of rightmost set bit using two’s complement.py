# Python Code for Position
# of rightmost set bit

import math


def getFirstSetBitPos(n):

	return math.log2(n & -n)+1

# driver code


n = 18
print(int(getFirstSetBitPos(n)))

# This code is contributed
# by Anant Agarwal.
