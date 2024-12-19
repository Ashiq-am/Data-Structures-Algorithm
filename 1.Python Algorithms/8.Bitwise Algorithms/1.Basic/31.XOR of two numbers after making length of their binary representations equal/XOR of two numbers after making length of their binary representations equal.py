# Python 3 implementation to return XOR
# of two numbers after making length
# of their binary representation same

# Function to count the number of bits
# in binary representation of an integer
def count(n):
    # initialize count
    c = 0

    # count till n is non zero
    while (n != 0):
        c += 1

        # right shift by 1
        # i.e, divide by 2
        n = n >> 1

    return c


# Function to calculate the xor of
# two numbers by adding trailing
# zeros to the number having less number
# of bits in its binary representation.
def XOR(a, b):
    # stores the minimum and maximum
    c = min(a, b)
    d = max(a, b)

    # left shift if the number of bits
    # are less in binary representation
    if (count(c) < count(d)):
        c = c << (count(d) - count(c))

    return (c ^ d)


# Driver Code
a = 13;
b = 5
print(XOR(a, b))

# This code is contributed by Nikita Tiwari.
