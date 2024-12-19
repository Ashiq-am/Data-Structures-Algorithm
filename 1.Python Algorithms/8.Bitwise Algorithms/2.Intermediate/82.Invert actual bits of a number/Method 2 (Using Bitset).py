# Python 3 program to invert actual
# bits of a number.
import math


def invertBits(num):
    # calculating number of
    # bits in the number
    x = int(math.log(num, 2.0) + 1)

    # Inverting the bits
    # one by one
    for i in range(0, x):
        num = (num ^ (1 << i))

    print(num)


# Driver code
num = 11
invertBits(num)

# This code is contributed
# by Akanksha Rai
