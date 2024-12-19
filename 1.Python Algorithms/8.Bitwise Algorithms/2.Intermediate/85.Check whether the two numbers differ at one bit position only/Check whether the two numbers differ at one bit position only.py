# Python3 implementation to check whether the two
# numbers differ at one bit position only

# function to check if x is power of 2
def isPowerOfTwo(x):
    # First x in the below expression is
    # for the case when x is 0
    return x and (not (x & (x - 1)))


# function to check whether the two numbers
# differ at one bit position only
def differAtOneBitPos(a, b):
    return isPowerOfTwo(a ^ b)


# Driver code to test above
a = 13
b = 9
if (differAtOneBitPos(a, b)):
    print("Yes")
else:
    print("No")

# This code is contributed by "Sharad_Bhardwaj".
