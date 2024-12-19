# Python3 implementation to
# pr numbers in the range
# 1 to n having first and
# last bits as the only set bits


# function to print numbers in the
# range 1 to n having first and
# last bits as the only set bits
def prNumWithFirstLastBitsSet(n):
    power_2 = 1

    # first number is '1'
    print(power_2, end=' ')

    while (1):
        # obtaining next perfect
        # power of 2
        power_2 <<= 1

        # toggling the last bit to
        # convert it to as set bit
        num = power_2 ^ 1

        # if out of range then break;
        if (n < num):
            break

        # display
        print(num, end=' ')


# Driver program
n = 10;
prNumWithFirstLastBitsSet(n)

# This code is contributed by saloni1297
