# An efficient Python 3 program
# to check Bleak Number
import math


# Function to get no of set
# bits in binary representation
# of passed binary no.
def countSetBits(x):
    count = 0

    while (x):
        x = x & (x - 1)
        count = count + 1

    return count


# A function to return ceiling
# of log x in base 2. For
# example, it returns 3 for 8
# and 4 for 9.
def ceilLog2(x):
    count = 0
    x = x - 1

    while (x > 0):
        x = x >> 1
        count = count + 1

    return count


# Returns true if n is Bleak
def isBleak(n):
    # Check for all numbers 'x'
    # smaller than n. If x +
    # countSetBits(x) becomes n,
    # then n can't be Bleak
    for x in range((n - ceilLog2(n)), n):

        if (x + countSetBits(x) == n):
            return False

    return True


# Driver code
if (isBleak(3)):
    print("Yes")
else:
    print("No")

if (isBleak(4)):
    print("Yes")
else:
    print("No")

# This code is contributed by Nikita Tiwari.
