# python 3 Program to Check if binary representation
# of a number is palindrome
import sys


# This function returns true if k'th bit in x
# is set (or 1). For example if x (0010) is 2
# and k is 2, then it returns true
def isKthBitSet(x, k):
    if ((x & (1 << (k - 1))) != 0):
        return True
    else:
        return False


# This function returns true if binary
# representation of x is palindrome.
# For example (1000...001) is palindrome
def isPalindrome(x):
    l = 1  # Initialize left position
    r = 2 * 8  # initialize right position

    # One by one compare bits
    while (l < r):
        if (isKthBitSet(x, l) != isKthBitSet(x, r)):
            return False
        l += 1
        r -= 1

    return True


# Driver Code
if __name__ == '__main__':
    x = 1 << 15 + 1 << 16
    print(int(isPalindrome(x)))
    x = 1 << 31 + 1
    print(int(isPalindrome(x)))

# This code is contributed by
# Surendra_Gangwar
