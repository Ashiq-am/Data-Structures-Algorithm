# Python 3 implementation to check whether
# all the bits are unset in the given range
# or not

# function to check whether all the bits
# are unset in the given range or not
def allBitsSetInTheGivenRange(n, l, r):
    # calculating a number 'num' having 'r'
    # number of bits and bits in the range l
    # to r are the only set bits
    num = ((1 << r) - 1) ^ ((1 << (l - 1)) - 1)

    # new number which will only have
    # one or more set bits in the
    # range l to r and nowhere else
    new_num = n & num

    # if new num is 0, then all bits
    # are unset in the given range
    if (new_num == 0):
        return "Yes"

    # else all bits are not unset
    return "No"


# Driver Code
if __name__ == "__main__":
    n = 17
    l = 2
    r = 4
    print(allBitsSetInTheGivenRange(n, l, r))

# This code is contributed by ita_c
