# A Python 3 program toggle bits of n2
# that are at same position as set
# bits of n1.


# function for the Nega_bit
def toggleBits(n1, n2):
    return (n1 ^ n2)


# Driver program to test above
n1 = 2
n2 = 5

print(toggleBits(n1, n2))

# This code is contributed
# by Nikita Tiwari.
