# Python3 program to count numbers whose bitwise
# XOR and sum with x are equal

# Function to find total 0 bit in a number


def CountZeroBit(x):
    count = 0
    while (x):

        if ((x & 1) == 0):
            count += 1
        x >>= 1

    return count


# Function to find Count of non-negative numbers
# less than or equal to x, whose bitwise XOR and
# SUM with x are equal.


def CountXORandSumEqual(x):
    # count number of zero bit in x
    count = CountZeroBit(x)

    # power of 2 to count
    return (1 << count)


# Driver code
if __name__ == '__main__':
    x = 10

    # Function call
    print(CountXORandSumEqual(x))

# This code is contributed by 29AjayKumar
