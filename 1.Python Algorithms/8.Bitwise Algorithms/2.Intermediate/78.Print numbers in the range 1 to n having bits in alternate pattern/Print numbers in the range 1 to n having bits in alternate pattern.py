# Python3 program for count total
# zero in product of array

# function to print numbers in the range
# 1 to nhaving bits in alternate pattern
def printNumHavingAltBitPatrn(n):
    # first number having bits in
    # alternate pattern
    curr_num = 1

    # display
    print(curr_num)

    # loop until n < curr_num
    while (1):

        # generate next number having
        # alternate bit pattern
        curr_num = curr_num << 1;

        # if true then break
        if (n < curr_num):
            break;

        # display
        print(curr_num)

        # generate next number having
        # alternate bit pattern
        curr_num = ((curr_num) << 1) ^ 1;

        # if true then break
        if (n < curr_num):
            break

        # display
        print(curr_num)


# Driven code
n = 50
printNumHavingAltBitPatrn(n)

# This code is contributed by "rishabh_jain".
