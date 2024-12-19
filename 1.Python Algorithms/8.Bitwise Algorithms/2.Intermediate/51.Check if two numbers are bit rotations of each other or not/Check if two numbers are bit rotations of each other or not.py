# Python3 program to check if two
# numbers are bit rotations of each other.

# function to check if two numbers
# are equal after bit rotation
def isRotation(x, y):
    # x64 has concatenation of x
    # with itself.
    x64 = x | (x << 32)

    while (x64 >= y):

        # comparing only last 32 bits
        if ((x64) == y):
            return True

        # right shift by 1 unit
        x64 >>= 1

    return False


# Driver Code
if __name__ == "__main__":

    x = 122
    y = 2147483678

    if (isRotation(x, y) == False):
        print("yes")
    else:
        print("no")

# This code is contributed by Ryuga
