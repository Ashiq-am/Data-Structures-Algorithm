# Python 3 program to find minimum flips required
# to make all 1s in left and 0s in right.
import sys


def minimalFilps(bits):
    n = len(bits)

    # two arrays will keep the count for number
    # of 0s' and 1s' to be flipped while
    # traversing from left to right and right to
    # left respectively
    flipsFromLeft = [0 for i in range(n)]
    flipsFromRight = [0 for i in range(n)]

    # Fill flipsFromLeft[]
    flips = 0
    for i in range(0, n, 1):
        if (bits[i] == '0'):
            flips = flips + 1
        flipsFromLeft[i] = flips

    # Fill flipsFromRight[]
    flips = 0
    i = n - 1
    while (i >= 0):
        if (bits[i] == '1'):
            flips = flips + 1
        i = i - 1
        flipsFromRight[i] = flips

    # initialize minFlip to highest int value.
    # If sum of leftflip and rightFlip is smaller
    # than minflips, then update minFlips
    minFlips = sys.maxsize
    for i in range(1, n, 1):
        if (flipsFromLeft[i - 1] +
                flipsFromRight[i] < minFlips):
            minFlips = (flipsFromLeft[i - 1] +
                        flipsFromRight[i])

    return minFlips


# Driver code
if __name__ == '__main__':
    bits = "00001"
    print(minimalFilps(bits))

# This code is contributed by
# Surendra_Gangwar
