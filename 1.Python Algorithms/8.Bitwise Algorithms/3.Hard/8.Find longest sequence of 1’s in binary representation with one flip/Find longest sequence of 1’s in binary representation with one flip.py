# Python3 program to find maximum
# consecutive 1's in binary
# representation of a number
# after flipping one bit.
from ctypes import sizeof


def flipBit(a):
    # If all bits are l,
    # binary representation
    # of 'a' has all 1s
    if (~a == 0):
        return 8 * sizeof()

    currLen = 0
    prevLen = 0
    maxLen = 0
    while (a > 0):

        # If Current bit is a 1
        # then increment currLen++
        if ((a & 1) == 1):
            currLen += 1

        # If Current bit is a 0
        # then check next bit of a
        elif ((a & 1) == 0):

            # Update prevLen to 0
            # (if next bit is 0)
            # or currLen (if next
            # bit is 1). */
            prevLen = 0 if ((a & 2) == 0) else currLen

            # If two consecutively bits
            # are 0 then currLen also
            # will be 0.
            currLen = 0

        # Update maxLen if required
        maxLen = max(prevLen + currLen, maxLen)

        # Remove last bit (Right shift)
        a >>= 1

    # We can always have a sequence
    # of at least one 1, this is
    # flipped bit
    return maxLen + 1


# Driver code
# input 1
print(flipBit(13))
# input 2
print(flipBit(1775))

# input 3
print(flipBit(15))


