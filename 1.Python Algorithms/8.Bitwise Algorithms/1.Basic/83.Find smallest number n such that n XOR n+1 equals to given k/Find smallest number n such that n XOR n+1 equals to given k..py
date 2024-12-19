# python to find n such that
# XOR of n and n+1 is equals
# to given n

# function to return the
# required n
def xorCalc(k):
    if (k == 1):
        return 2

    # if k is of form 2^i-1
    if (((k + 1) & k) == 0):
        return k / 2

    return 1;


# driver program
k = 31
print(int(xorCalc(k)))

# This code is contributed
# by Sam007
