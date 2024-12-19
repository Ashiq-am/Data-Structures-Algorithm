# Python3 for finding min flip
# for maximizing given n
import math


# function for finding set bit
def setBit(xorValue):
    count = 0
    while (xorValue):
        if (xorValue % 2):
            count += 1

        xorValue = int(xorValue / 2)

    # return count
    # of set bit
    return count


# function for
# finding min flip
def minFlip(n, k):
    # number of bits in n
    size = int(math.log(n) /
               math.log(2) + 1)

    # Find the largest number of
    # same size with k set bits
    max = pow(2, k) - 1
    max = max << (size - k)

    # Count bit differences to
    # find required flipping.
    xorValue = (n ^ max)
    return (setBit(xorValue))


# Driver Code
n = 27
k = 3
print("Min Flips = ",
      minFlip(n, k))

# This code is contributed
# by Smitha
