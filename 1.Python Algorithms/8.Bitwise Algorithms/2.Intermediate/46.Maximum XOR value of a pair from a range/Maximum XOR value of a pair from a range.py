# Python3 program to get maximum xor
# value of two numbers in a range

# Method to get maximum xor
# value in range [L, R]
def maxXORInRange(L, R):
    # get xor of limits
    LXR = L ^ R

    # loop to get msb position of L^R
    msbPos = 0
    while (LXR):
        msbPos += 1
        LXR >>= 1

    # construct result by adding 1,
    # msbPos times
    maxXOR, two = 0, 1

    while (msbPos):
        maxXOR += two
        two <<= 1
        msbPos -= 1

    return maxXOR


# Driver code
L, R = 8, 20
print(maxXORInRange(L, R))

# This code is contributed by Anant Agarwal.
