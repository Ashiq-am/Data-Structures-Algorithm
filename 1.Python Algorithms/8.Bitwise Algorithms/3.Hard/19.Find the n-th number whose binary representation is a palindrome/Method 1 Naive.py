# Python 3 program to find n-th number
# whose binary representation is palindrome.
INT_MAX = 2147483647


# Finds if the kth bit is set in
# the binary representation


def isKthBitSet(x, k):
    return 1 if (x & (1 << (k - 1))) else 0


# Returns the position of leftmost
# set bit in the binary representation


def leftmostSetBit(x):
    count = 0
    while (x):
        count += 1
        x = x >> 1

    return count


# Finds whether the integer in binary
# representation is palindrome or not


def isBinPalindrome(x):
    l = leftmostSetBit(x)
    r = 1

    # One by one compare bits
    while (l > r):

        # Compare left and right bits
        # and converge
        if (isKthBitSet(x, l) != isKthBitSet(x, r)):
            return 0
        l -= 1
        r += 1
    return 1


def findNthPalindrome(n):
    pal_count = 0

    # Start from 1, traverse
    # through all the integers
    i = 0
    for i in range(1, INT_MAX + 1):
        if (isBinPalindrome(i)):
            pal_count += 1

        # If we reach n, break the loop
        if (pal_count == n):
            break

    return i


# Driver code
if __name__ == "__main__":
    n = 9

    # Function Call
    print(findNthPalindrome(n))
