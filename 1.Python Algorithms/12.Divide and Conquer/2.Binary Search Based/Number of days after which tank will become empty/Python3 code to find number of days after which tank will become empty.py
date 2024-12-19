# Python3 code to find number of days
# after which tank will become empty
import math


# Method returns minimum number of days
# after which tank will become empty
def minDaysToEmpty(C, l):
    if (l >= C): return C

    eq_root = (math.sqrt(1 + 8 * (C - l)) - 1) / 2
    return math.ceil(eq_root) + l


# Driver code
print(minDaysToEmpty(5, 2))
print(minDaysToEmpty(6514683, 4965))

# This code is contributed by Smitha Dinesh Semwal.
