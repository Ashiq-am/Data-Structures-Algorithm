# Python3 program to find the
# position of first rightmost
# set bit in a given number
import math


# Function to find rightmost
# set bit in given number.
def getFirstSetBitPos(n):
    return int(math.log2(n & -n) + 1)


# Driver Code
if __name__ == '__main__':
    n = 12
    print(getFirstSetBitPos(n))

# This code is contributed by nirajgusain5.
