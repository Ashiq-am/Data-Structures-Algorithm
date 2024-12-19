# Python program to check
# if given number is
# power of 4 or not
# Function to check perfect square
# import the math module
import math


def isPerfectSquare(n):
    x = math.sqrt(n)
    return (x * x == n)


def isPowerOfFour(n):
    # If n <= 0, it is not the power of four
    if (n <= 0):
        return False

    # Check whether 'n' is a perfect square or not
    if (isPerfectSquare(n)):
        return False

    # If 'n' is the perfect square
    # Check for the second condition i.e. 'n' must be power of two
    return (n & (n - 1))


# Driver code
test_no = 64
if (isPowerOfFour(test_no)):
    print(test_no, " is a power of 4")
else:
    print(test_no, " is not a power of 4")

# This code is contributed by shivanisinghss2110
