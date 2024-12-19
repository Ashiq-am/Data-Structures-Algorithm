# An efficient Python program to find bit-wise & of
# all numbers from x to y.

# Importing math module for using logarithm
import math


# Function to find Bit-wise & of all numbers from x
# to y.
def andOperator(x, y):
    # Iterate over all bits of y, starting from the lsb, if it's equal to 1, flip it
    for i in range(int(math.log2(y) + 1)):

        # repeat till x >= y, otherwise return the answer
        if (y <= x):
            return y
        if (y & 1 << i):
            y = y & (~(1 << i))
    return y


# Driver code
x, y = 10, 15
print(andOperator(x, y))

# This code is contributed by Pushpesh Raj
