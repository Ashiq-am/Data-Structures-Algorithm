# Python3 implementation to check
# whether n is divisible by pow(2, m)

# function to check whether n
# is divisible by pow(2, m)
def isDivBy2PowerM(n, m):
    # if expression results to 0, then
    # n is divisible by pow(2, m)
    if (n & ((1 << m) - 1)) == 0:
        return True

    # n is not divisible
    return False


# Driver program to test above
n = 8
m = 2
if isDivBy2PowerM(n, m):
    print("Yes")
else:
    print("No")

# This code is contributed by "Sharad_Bhardwaj".
