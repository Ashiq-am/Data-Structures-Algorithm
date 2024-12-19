# Python implementation
# to set the kth bit
# of the given number

# function to set
# the kth bit
def setKthBit(n, k):
    # kth bit of n is being
    # set by this operation
    return ((1 << k) | n)


# Driver code

n = 10
k = 2

print("Kth bit set number = ",
      setKthBit(n, k))

# This code is contributed
# by Anant Agarwal.
