# Python3 implementation to find
# the previous smaller integer with
# one less number of set bits
import math


# Function to find the position
# of rightmost set bit.
def getFirstSetBitPos(n):
    return (int)(math.log(n & -n) /
                 math.log(2)) + 1


# Function to find the
# previous smaller integer
def previousSmallerInteger(n):
    # position of rightmost set bit of n
    pos = getFirstSetBitPos(n)

    # turn off or unset the bit
    # at position 'pos'
    return (n & ~(1 << (pos - 1)))


# Driver code
n = 25
print("Previous small Integer = ",
      previousSmallerInteger(n))

# This code is contributed by Anant Agarwal.
