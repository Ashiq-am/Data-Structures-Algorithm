# Python implementation to check if a number
# has bits in alternate pattern

# function to check if all the bits are set or not
# in the binary representation of 'n'
def allBitsAreSet(n):
    # if true, then all bits are set
    if (((n + 1) & n) == 0):
        return True;

    # else all bits are not set
    return False;


# function to check if a number
# has bits in alternate pattern
def bitsAreInAltOrder(n):
    num = n ^ (n >> 1);

    # to check if all bits are set
    # in 'num'
    return allBitsAreSet(num);


# Driver code
n = 10;

if (bitsAreInAltOrder(n)):
    print("Yes");
else:
    print("No");

# This code is contributed by PrinciRaj1992
