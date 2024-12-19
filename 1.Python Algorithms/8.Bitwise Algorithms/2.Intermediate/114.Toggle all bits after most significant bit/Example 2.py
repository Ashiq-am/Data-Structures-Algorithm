# Python program to toggle set bits starting
# from MSB

# Returns a number which has all set bits
# starting from MSB of n
def setAllBitsAfterMSB(n):
    # This makes sure two bits
    # (From MSB and including MSB)
    # are set
    n |= n >> 1

    # This makes sure 4 bits
    # (From MSB and including MSB)
    # are set
    n |= n >> 2

    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    return n


def toggle(n):
    n = n ^ setAllBitsAfterMSB(n)
    return n


# Driver code

n = 10
n = toggle(n)
print(n)
# This code is contributed by Anant Agarwal.
