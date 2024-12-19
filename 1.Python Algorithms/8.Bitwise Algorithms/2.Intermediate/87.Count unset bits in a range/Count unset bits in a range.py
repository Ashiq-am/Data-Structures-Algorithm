# Python3 implementation to count
# unset bits in the given range

# Function to get no of set bits in
# the binary representation of 'n'
def countSetBits(n):
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count


# function to count unset bits
# in the given range
def countUnsetBitsInGivenRange(n, l, r):
    # calculating a number 'num' having
    # 'r' number of bits and bits in the
    # range l to r are the only set bits
    num = ((1 << r) - 1) ^ ((1 << (l - 1)) - 1)

    # returns number of unset bits
    # in the range 'l' to 'r' in 'n'
    return (r - l + 1) - countSetBits(n & num)


# Driver code to test above
n = 80
l = 1
r = 4
print(countUnsetBitsInGivenRange(n, l, r))

# This code is contributed by "Sharad_Bhardwaj"
