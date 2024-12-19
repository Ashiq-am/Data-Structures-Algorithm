import os
import sys

# This function will return absolute value of n
def getAbs(n):
    mask = n >> (sys.getsizeof(int()) * os.sysconf('SC_CHAR_BIT') - 1)
    return ((n ^ mask) - mask)

# Driver code
n = -6
print("The absolute value of", n, "is", getAbs(n))

# This code is contributed by phalasi.
