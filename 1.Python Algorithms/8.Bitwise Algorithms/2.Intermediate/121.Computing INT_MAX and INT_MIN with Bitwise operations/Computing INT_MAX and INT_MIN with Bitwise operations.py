# Python3 code to compute INT_MAX and INT_MIN using
# bitwise operations
def printMinMaxValues():
    # 0 saved as unsigned int
    max = 0

    # Computing NOT of 0
    # to signed integer to unsigned integer
    # in Python3, add 1 << 32 to the integer
    max = ~max + (1 << 32)

    # 1 time arithmetic right shift
    max = max >> 1

    # Computing INT_MIN
    min = max;

    # INT_MIN = ~INT_MAX
    min = ~min

    # Printing the result
    print("INT_MAX :", max, "INT_MIN :", min)


# Driver code
printMinMaxValues()

# This code is contributed by phasing17
