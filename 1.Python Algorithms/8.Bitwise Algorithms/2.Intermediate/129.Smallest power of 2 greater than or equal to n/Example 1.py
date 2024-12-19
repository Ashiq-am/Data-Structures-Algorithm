def nextPowerOf2(n):
    count = 0

    # First n in the below
    # condition is for the
    # case where n is 0
    if (n and not (n & (n - 1))):
        return n

    while (n != 0):
        n >>= 1
        count += 1

    return 1 << count


# Driver Code
n = 0
print(nextPowerOf2(n))
# This code is contributed
# by Smitha Dinesh Semwal
