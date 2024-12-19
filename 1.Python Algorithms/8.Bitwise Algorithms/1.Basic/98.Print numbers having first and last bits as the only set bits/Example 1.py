# Python implementation to print
# numbers in the range 1 to n
# having first and last bits
# as the only set bits
import math


# function to check whether 'n'
# is a power of 2 or not
def powerOfTwo(n):
    re = (n & n - 1)
    return (re == 0)


# function to print numbers
# in the range 1 to n having
# first and last bits as
# the only set bits
def printNumWithFirstLastBitsSet(n):
    i = 1

    # first number is '1'
    print(i, end=" ")

    # generating all the numbers
    for i in range(3, n + 1):

        # if true, then print 'i'
        if (powerOfTwo(i - 1)):
            print(i, end=" ")


# driver function
n = 10
printNumWithFirstLastBitsSet(n)

# This code is contributed by Gitanjali.
