# This function returns next
# higher number with same
# number of set bits as x.
def snoob(x):
    next = 0
    if (x):
        # right most set bit
        rightOne = x & -(x)

        # reset the pattern and
        # set next higher bit
        # left part of x will
        # be here
        nextHigherOneBit = x + int(rightOne)

        # nextHigherOneBit is
        # now part [D] of the
        # above explanation.
        # isolate the pattern
        rightOnesPattern = x ^ int(nextHigherOneBit)

        # right adjust pattern
        rightOnesPattern = (int(rightOnesPattern) /
                            int(rightOne))

        # correction factor
        rightOnesPattern = int(rightOnesPattern) >> 2

        # rightOnesPattern is now part
        # [A] of the above explanation.

        # integrate new pattern
        # (Add [D] and [A])
        next = nextHigherOneBit | rightOnesPattern
    return next


# Driver Code
x = 156
print("Next higher number with " +
      "same number of set bits is",
      snoob(x))
