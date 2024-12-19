# Python3 program to invert actual
# bits of a number.
import math


def invertBits(num):
    # calculating number of bits
    # in the number
    x = int(math.log2(num)) + 1

    # Inverting the bits one by one
    for i in range(x):
        num = (num ^ (1 << i))

    print(num)


# Driver Code
num = 11
invertBits(num)

# This code is contributed
# by Rituraj Jain
