# Python3 program to check if counts of
# consecutive 1s are increasing order.

import sys


# Returns true if n has counts of
# consecutive 1's are increasing order.
def areSetBitsIncreasing(n):
    # Initialize previous count
    prev_count = sys.maxsize

    # We traverse bits from right to
    # left and check if counts are
    # decreasing order.
    while (n > 0):

        # Ignore 0s until we reach a
        # set bit.
        while (n > 0 and n % 2 == 0):
            n = int(n / 2)

        # Count current set bits
        curr_count = 1
        while (n > 0 and n % 2 == 1):
            n = n / 2
            curr_count += 1

        # Compare current with previous
        # and update previous.
        if (curr_count >= prev_count):
            return False
        prev_count = curr_count

    return True


# Driver code
n = 10

if (areSetBitsIncreasing(n)):
    print("Yes")
else:
    print("No")

# This code is contributed by Smitha
