# python 3 implementation
# to increment a number
# by one by manipulating
# the bits
import math


# function to find the
# position of rightmost
# set bit
def getPosOfRightmostSetBit(n):
    return math.log2(n & -n)


# function to toggle the last m bits
def toggleLastKBits(n, k):
    # calculating a number
    # 'num' having 'm' bits
    # and all are set
    num = (1 << (int)(k)) - 1

    # toggle the last m bits and
    # return the number
    return (n ^ num)


# function to increment
# a number by one by
# manipulating the bits
def incrementByOne(n):
    # get position of rightmost
    # unset bit if all bits of
    # 'n' are set, then the bit
    # left to the MSB is the
    # rightmost unset bit
    k = getPosOfRightmostSetBit(~n)

    # kth bit of n is being
    # set by this operation
    n = ((1 << (int)(k)) | n)

    # from the right toggle
    # all the bits before the
    # k-th bit
    if (k != 0):
        n = toggleLastKBits(n, k)

    # required number
    return n


# Driver program
n = 15
print(incrementByOne(n))

# This code is contributed
# by Nikita Tiwari.
