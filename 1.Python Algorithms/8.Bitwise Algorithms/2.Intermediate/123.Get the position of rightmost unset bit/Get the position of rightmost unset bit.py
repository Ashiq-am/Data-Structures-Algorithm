# Python3 implementation to get the position
# of rightmost unset bit

# import library
import math as m


# function to find the position
# of rightmost set bit
def getPosOfRightmostSetBit(n):
    return (m.log(((n & - n) + 1), 2))


# function to get the position ot rightmost unset bit
def getPosOfRightMostUnsetBit(n):
    # if n = 0, return 1
    if (n == 0):
        return 1

    # if all bits of 'n' are set
    if ((n & (n + 1)) == 0):
        return -1

    # position of rightmost unset bit in 'n'
    # passing ~n as argument
    return getPosOfRightmostSetBit(~n)


# Driver program to test above
n = 13;
ans = getPosOfRightMostUnsetBit(n)

# rounding the final answer
print(round(ans))

# This code is contributed by Saloni Gupta.
