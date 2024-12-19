# Python program to count numbers whose
# XOR with n produces a value more than n.

def countNumbers(n):
    ''' If there is a number like m = 11110000,
    then it is bigger than 1110xxxx. x can either
    0 or 1. So we have pow(2, k) greater numbers
    where k is position of rightmost 1 in m. Now
    by using XOR bit at each position can be changed.
    To change bit at any position, it needs to XOR
    it with 1. '''

    # Position of current bit in n
    k = 0

    # Traverse bits from
    # LSB to MSB
    count = 0  # Initialize result
    while (n > 0):

        # If current bit is 0, then there are
        # 2^k numbers with current bit 1 and
        # whose XOR with n produces greater value
        if ((n & 1) == 0):
            count += pow(2, k)

        # Increase position for next bit
        k += 1

        # Reduce n to find next bit
        n >>= 1

    return count


# Driver code
n = 11
print(countNumbers(n))

# This code is contributed by Anant Agarwal.
