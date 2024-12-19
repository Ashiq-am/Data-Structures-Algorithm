# Python 3 program to toggle first
# and last bits of a number.


# Returns a number which has same bit
# count as n and has only first and last
# bits as set.
def takeLandFsetbits(n):
    # set all the bit of the number
    n = n | n >> 1
    n = n | n >> 2
    n = n | n >> 4
    n = n | n >> 8
    n = n | n >> 16

    # Adding one to n now unsets
    # all bits and moves MSB to
    # one place. Now we shift
    # the number by 1 and add 1.
    return ((n + 1) >> 1) + 1


def toggleFandLbits(n):
    # if number is 1
    if (n == 1):
        return 0

    # take XOR with first and
    # last set bit number
    return n ^ takeLandFsetbits(n)


# Driver code
n = 10
print(toggleFandLbits(n))

# This code is contributed by Nikita Tiwari.
