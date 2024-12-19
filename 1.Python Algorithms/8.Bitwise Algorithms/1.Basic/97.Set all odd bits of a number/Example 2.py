# Efficient python3 program to
# set all odd bits number
import math


# return MSB set number
def getmsb(n):
    # set all bits including MSB.
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16

    # return MSB
    return (n + 1) >> 1


# Returns a number of same
# size (MSB at same position)
# as n and all odd bits set.
def getevenbits(n):
    n = getmsb(n)

    # generate odd bits
    # like 010101..
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16

    # if bits is even
    # then shift by 1
    if ((n & 1) == 0):
        n = n >> 1

    # return odd set bits number
    return n


# set all odd bits here
def setalloddbits(n):
    # take OR with odd
    # set bits number
    return n | getevenbits(n)


# Driver Program
n = 10
print(setalloddbits(n))

# This code is contributed
# by Gitanjali.
