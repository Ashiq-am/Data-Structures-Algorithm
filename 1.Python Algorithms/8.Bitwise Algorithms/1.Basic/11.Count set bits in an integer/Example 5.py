# Python implementation of the approach
BitsSetTable256 = [0] * 256


# Function to initialise the lookup table
def initialize():
    # To initially generate the
    # table algorithmically
    BitsSetTable256[0] = 0
    for i in range(256):
        BitsSetTable256[i] = (i & 1) + BitsSetTable256[i // 2]


# Function to return the count
# of set bits in n
def countSetBits(n):
    return (BitsSetTable256[n & 0xff] +
            BitsSetTable256[(n >> 8) & 0xff] +
            BitsSetTable256[(n >> 16) & 0xff] +
            BitsSetTable256[n >> 24])


# Driver code

# Initialise the lookup table
initialize()
n = 9
print(countSetBits(n))

# This code is contributed by SHUBHAMSINGH10
