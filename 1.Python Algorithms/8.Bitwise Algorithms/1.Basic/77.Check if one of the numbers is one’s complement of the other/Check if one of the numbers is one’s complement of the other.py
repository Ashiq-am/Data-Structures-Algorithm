# Python3 implementation to
# check if one of the two
# numbers is one's complement
# of the other


# function to check if
# all the bits are set
# or not in the binary
# representation of 'n'
def areAllBitsSet(n):
    # all bits are not set
    if (n == 0):
        return False;

    # if True, then all bits are set
    if (((n + 1) & n) == 0):
        return True;

    # else all bits are not set
    return False;


# function to check if one
# of the two numbers is
# one's complement of the other
def isOnesComplementOfOther(a, b):
    return areAllBitsSet(a ^ b)


# Driver program
a = 1
b = 14
if (isOnesComplementOfOther(a, b)):
    print("Yes")
else:
    print("No")

# This code is contributed by
# Saloni Gupta 4
