# python implementation to unset bits
# in the given range

# Function to toggle bits in the
# given range
def toggleBitsFromLToR(n, l, r):
    # calculating a number 'num'
    # having 'r' number of bits
    # and bits in the range l to
    # r are the only set bits
    num = (((1 << r) - 1) ^
           ((1 << (l - 1)) - 1))

    # toggle the bits in the range
    # l to r in 'n' and return the
    # number
    return (n ^ num)


# Function to unset bits in the
# given range
def unsetBitsInGivenRange(n, l, r):
    # 'num' is the highest positive
    # integer number all the bits
    # of 'num' are set
    num = (1 << (4 * 8 - 1)) - 1

    # toggle the bits in the range
    # l to r in 'num'
    num = toggleBitsFromLToR(num, l, r)

    # unset the bits in the range
    # l to r in 'n' and return the
    # number
    return (n & num)


# Driver code
n = 42
l = 2
r = 5
print(unsetBitsInGivenRange(n, l, r))

# This code is contributed by Sam007.
