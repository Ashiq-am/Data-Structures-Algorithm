# Python3 program to check
# if given number is
# power of 4 or not
import math


def logn(n, r):
    return math.log(n) / math.log(r)


def isPowerOfFour(n):
    # 0 is not considered
    # as a power of 4
    if (n == 0):
        return False

    return (math.floor(logn(n, 4)) ==
            math.ceil(logn(n, 4)))


# Driver code
if __name__ == '__main__':

    test_no = 64

    if (isPowerOfFour(test_no)):
        print(test_no, " is a power of 4")
    else:
        print(test_no, " is not a power of 4")

# This code is contributed by Amit Katiyar
