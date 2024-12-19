# Python program for above approach

# Program to find position of
# rightmost set bit
def PositionRightmostSetbit(n):
    p = 1

    # Iterate till number>0
    while (n > 0):

        # Checking if last bit is set
        if (n & 1):
            return p

        # Increment position and right shift number
        p += 1
        n = n >> 1

    # set bit not found.
    return -1;

# Driver Code
n = 18
# Function call
pos = PositionRightmostSetbit(n)
if (pos != -1):
    print(pos)
else:
    print(0)

# This code is contributed by rohitsingh07052.
