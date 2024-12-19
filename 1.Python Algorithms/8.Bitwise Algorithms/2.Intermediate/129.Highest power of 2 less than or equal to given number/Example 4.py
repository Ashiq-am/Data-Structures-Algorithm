# Python3 program to find highest power of 2 smaller than or equal to n.

def highestPowerof2(x):
    # check for the set bits
    x |= x >> 1
    x |= x >> 2
    x |= x >> 4
    x |= x >> 8
    x |= x >> 16

    # Then we remove all but the top bit by xor'ing the
    # string of 1's with that string of 1's shifted one to
    # the left, and we end up with just the one top bit
    # followed by 0's.
    return x ^ (x >> 1)


n = 10
print(highestPowerof2(n))

# This code is contributed by divyesh072019.
