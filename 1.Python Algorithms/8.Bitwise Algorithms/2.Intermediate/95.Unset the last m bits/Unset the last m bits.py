# Python3 implementation to unset
# bits the last m bits
import sys


# function to toggle the last m bits
def toggleLastMBits(n, m):
    # calculating a number 'num'
    # having 'm' bits and all are set
    num = (1 << m) - 1

    # toggle the last m bits
    # and return the number
    return (n ^ num)


# function to unset bits
# the last m bits
def unsetLastMBits(n, m):
    # 'num' is the highest positive integer
    # number all the bits of 'num' are set
    num = (1 << (sys.getsizeof(int) * 8 - 1)) - 1

    # toggle the last 'm' bits in 'num'
    num = toggleLastMBits(num, m)

    # unset the last 'm' bits in 'n'
    # and return the number
    return (n & num)


# Driven code
n = 150
m = 4
print(unsetLastMBits(n, m))

# This code is contributed by "rishabh_jain".
