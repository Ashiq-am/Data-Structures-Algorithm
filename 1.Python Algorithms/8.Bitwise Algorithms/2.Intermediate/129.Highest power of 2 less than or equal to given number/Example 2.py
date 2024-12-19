# Python3 program to find highest power of 2 smaller
# than or equal to n.

import sys


def highestPowerof2(n):
    # Invalid input
    if (n < 1):
        return 0

    res = 1

    # Try all powers starting from 2^1
    for i in range(8 * sys.getsizeof(n)):

        curr = 1 << i

        # If current power is more than n, break
        if (curr > n):
            break

        res = curr

    return res


# Driver code
if __name__ == "__main__":
    n = 10
    print(highestPowerof2(n))

