# Python3 implementation to find
# the next greater integer with
# one more number of set bits
import math


# Function to find the position
# of rightmost set bit. Returns -1
# if there are no set bits
def getFirstSetBitPos(n):
    return ((int)(math.log(n & -n) /
                  math.log(2)) + 1) - 1


# Function to find the next greater integer
def nextGreaterWithOneMoreSetBit(n):
    # position of rightmost unset bit of
    # n by passing ~n as argument
    pos = getFirstSetBitPos(~n)

    # if n consists of unset bits, then
    # set the rightmost unset bit
    if (pos > -1):
        return (1 << pos) | n

    # n does not consists of unset bits
    return ((n << 1) + 1)


# Driver code
n = 10
print("Next greater integer = ",
      nextGreaterWithOneMoreSetBit(n))

# This code is contributed by Anant Agarwal.
