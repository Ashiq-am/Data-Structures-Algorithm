# Python3 implementation to count
# set bits in the given range

# Function to get no of set bits in the
# binary representation of 'n'
def countSetBits(n):
    count = 0
    while (n):
        n &= (n - 1)
        count = count + 1

    return count


# function to count set bits in
# the given range
def countSetBitsInGivenRange(n, l, r):
    # calculating a number 'num' having
    # 'r' number of bits and bits in the
    # range l to r are the only set bits
    num = ((1 << r) - 1) ^ ((1 << (l - 1)) - 1)

    # returns number of set bits in the range
    # 'l' to 'r' in 'n'
    return countSetBits(n & num)


# Driver program to test above
n = 42
l = 2
r = 5
ans = countSetBitsInGivenRange(n, l, r)
print(ans)

# This code is contributed by Saloni Gupta.
