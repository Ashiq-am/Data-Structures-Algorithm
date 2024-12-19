# Iterative Python3 program
# to implement pow(x, n)

# Iterative Function to
# calculate (x^y) in O(logy)
def power(x, y):
    # Initialize result
    res = 1

    while (y > 0):

        # If y is odd, multiply
        # x with result
        if ((y & 1) == 1):
            res = res * x

        # n must be even
        # now y = y/2
        y = y >> 1

        # Change x to x^2
        x = x * x

    return res


# Driver Code
x = 3
y = 5

print("Power is ",power(x, y))
