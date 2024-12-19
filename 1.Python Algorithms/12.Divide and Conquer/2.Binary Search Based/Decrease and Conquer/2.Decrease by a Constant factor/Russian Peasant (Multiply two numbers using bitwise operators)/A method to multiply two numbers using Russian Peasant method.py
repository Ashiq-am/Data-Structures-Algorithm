# A method to multiply two numbers
# using Russian Peasant method

# Function to multiply two numbers
# using Russian Peasant method
def russianPeasant(a, b):
    res = 0  # initialize result

    # While second number doesn't
    # become 1
    while (b > 0):

        # If second number becomes
        # odd, add the first number
        # to result
        if (b & 1):
            res = res + a

        # Double the first number
        # and halve the second
        # number
        a = a << 1
        b = b >> 1

    return res


# Driver program to test
# above function
print(russianPeasant(18, 1))
print(russianPeasant(20, 12))
# This code is contributed by
# Smitha Dinesh Semwal
