# Python3 implementation to find the position
# of rightmost same bit

# Function to find the position of
# rightmost same bit in the
# binary representations of 'm' and 'n'
def posOfRightMostSameBit(m, n):
    # Initialize loop counter
    loopCounter = 1

    while (m > 0 or n > 0):

        # Check whether the value 'm' is odd
        a = m % 2 == 1

        # Check whether the value 'n' is odd
        b = n % 2 == 1

        # Below 'if' checks for both
        # values to be odd or even
        if (not (a ^ b)):
            return loopCounter

        # Right shift value of m
        m = m >> 1

        # Right shift value of n
        n = n >> 1
        loopCounter += 1

    # When no common set is found
    return -1


# Driver code
if __name__ == '__main__':
    m, n = 16, 7

    print("Position = ",
          posOfRightMostSameBit(m, n))

# This code is contributed by mohit kumar 29
