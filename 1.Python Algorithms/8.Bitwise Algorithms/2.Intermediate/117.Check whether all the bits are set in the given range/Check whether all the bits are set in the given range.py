# Python3 implementation to check
# whether all the bits are set in
# the given range or not

# Function to check whether all the bits
# are set in the given range or not
def allBitsSetInTheGivenRange(n, l, r):
    # calculating a number 'num' having 'r'
    # number of bits and bits in the range l
    # to r are the only set bits
    num = ((1 << r) - 1) ^ ((1 << (l - 1)) - 1)

    # new number which will only have
    # one or more set bits in the range
    # l to r and nowhere else
    new_num = n & num

    # if both are equal, then all bits
    # are set in the given range
    if (num == new_num):
        return "Yes"

    # else all bits are not set
    return "No"


# Driver code
n, l, r = 22, 2, 3
print(allBitsSetInTheGivenRange(n, l, r))

# This code is contributed by Anant Agarwal.
