# Python3 implementation for
# recursive approach to find
# the number of set bits using
# Brian Kernighan’s Algorithm

# recursive function to count
# set bits
def countSetBits(n):
    # base case
    if (n == 0):
        return 0
    else:
        return 1 + countSetBits(n & (n - 1))


# Get value from user
n = 9

# function calling
print(countSetBits(n))

# This code is contributed by sunnysingh
