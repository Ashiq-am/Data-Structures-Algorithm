# Python3 implementation of the approach

# Function to check if n is power of 8
def checkPowerof8(n):
    # Variable i will denote the bit
    # that we are currently at
    i = 0
    l = 1

    while (i <= 63):
        l <<= i

        # If only set bit in n
        # is at position i
        if (l == n):
            return True

        # Get to next valid bit position
        i += 3
        l = 1

    return False


# Driver code
if __name__ == '__main__':

    n = 65
    if (checkPowerof8(n)):
        print("Yes")
    else:
        print("No")

# This code is contributed by math_lover
