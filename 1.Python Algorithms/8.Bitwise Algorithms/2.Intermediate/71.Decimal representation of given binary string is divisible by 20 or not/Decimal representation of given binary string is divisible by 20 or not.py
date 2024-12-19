# Python 3 implementation to check whether
# decimal representation of given binary
# number is divisible by 20 or not

# function to check whether decimal
# representation of given binary number
# is divisible by 10 or not
def isDivisibleBy10(bin, n):
    # if last digit is '1', then
    # number is not divisible by 10
    if (bin[n - 1] == '1'):
        return False

    # to accumulate the sum of last digits
    # in perfect powers of 2
    sum = 0

    # traverse from the 2nd last up
    # to 1st digit in 'bin'
    for i in range(n - 2, -1, -1):

        # if digit in '1'
        if (bin[i] == '1'):

            # calculate digit's position from
            # the right
            posFromRight = n - i - 1

            # according to the digit's position,
            # obtain the last digit of the
            # applicable perfect power of 2
            if (posFromRight % 4 == 1):
                sum = sum + 2
            elif (posFromRight % 4 == 2):
                sum = sum + 4
            elif (posFromRight % 4 == 3):
                sum = sum + 8
            elif (posFromRight % 4 == 0):
                sum = sum + 6

    # if last digit is 0, then
    # divisible by 10
    if (sum % 10 == 0):
        return True

    # not divisible by 10
    return False


# function to check whether decimal
# representation of given binary number
# is divisible by 20 or not
def isDivisibleBy20(bin, n):
    # if 'bin' is an odd number
    if (bin[n - 1] == '1'):
        return false

    # check if bin(0..n-2) is divisible
    # by 10 or not
    return isDivisibleBy10(bin, n - 1)


# Driver program to test above
bin = ['1', '0', '1', '0', '0', '0']
n = len(bin)
if (isDivisibleBy20(bin, n - 1)):
    print("Yes")
else:
    print("No")

# This code is contributed by Smitha Dinesh Semwal
