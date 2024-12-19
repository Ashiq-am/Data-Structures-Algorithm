# Python program to find position
# of only set bit in a given number

def Log2n(n):
    if (n > 1):
        return (1 + Log2n(n / 2))
    else:
        return 0


# A utility function to check
# whether n is power of 2 or not
def isPowerOfTwo(n):
    return n and (not (n & (n - 1)))


def findPosition(n):
    if (not isPowerOfTwo(n)):
        return -1
    return Log2n(n) + 1


# Driver program to test above function

n = 0
pos = findPosition(n)
if (pos == -1):
    print("n =", n, ", Invalid number")
else:
    print("n = ", n, ", Position ", pos)

n = 12
pos = findPosition(n)
if (pos == -1):
    print("n =", n, ", Invalid number")
else:
    print("n = ", n, ", Position ", pos)
n = 128
pos = findPosition(n)
if (pos == -1):
    print("n = ", n, ", Invalid number")
else:
    print("n = ", n, ", Position ", pos)

# This code is contributed
# by Sumit Sudhakar
