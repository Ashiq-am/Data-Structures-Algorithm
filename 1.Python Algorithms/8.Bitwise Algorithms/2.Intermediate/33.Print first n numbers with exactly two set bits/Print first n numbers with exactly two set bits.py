# Python3 program to print first n
# numbers with exactly two set bits

# Prints first n numbers
# with two set bits
def printTwoSetBitNums(n):
    # Initialize higher of
    # two sets bits
    x = 1

    # Keep reducing n for every
    # number with two set bits.
    while (n > 0):

        # Consider all lower set bits
        # for current higher set bit
        y = 0
        while (y < x):

            # Print current number
            print((1 << x) + (1 << y),
                  end=" ")

            # If we have found n numbers
            n -= 1
            if (n == 0):
                return

            # Consider next lower bit
            # for current higher bit.
            y += 1

        # Increment higher set bit
        x += 1


# Driver code
printTwoSetBitNums(4)

# This code is contributed
# by Smitha
