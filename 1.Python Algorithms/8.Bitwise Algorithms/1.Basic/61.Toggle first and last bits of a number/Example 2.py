# Python3 program to toggle first and last
# bits of a number
from math import log


# Function to toggle first and last bits
# of a number
def toggleFandLbits(n):
    # calculating mask
    mask = 2 ** (int(log(n, 2))) + 1

    # taking xor of mask and n
    return mask ^ n


# Driver code
n = 10

# Function call
print(toggleFandLbits(n))

# This code is contributed by phasing17
