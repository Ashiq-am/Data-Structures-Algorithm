def swapBits(num, p1, p2, n):
    shift1 = 0
    shift2 = 0
    value1 = 0
    value2 = 0

    while (n > 0):

        # Setting bit at p1 position to 1
        shift1 = 1 << p1

        # Setting bit at p2 position to 1
        shift2 = 1 << p2

        # value1 and value2 will have 0 if num
        # at the respective positions - p1 and p2 is 0.
        value1 = ((num & shift1))
        value2 = ((num & shift2))

        # check if value1 and value2 are different
        # i.e. at one position bit is set and other it is not
        if ((value1 == 0 and value2 != 0) or (value2 == 0 and value1 != 0)):

            # if bit at p1 position is set
            if (value1 != 0):

                # unset bit at p1 position
                num = num & (~shift1)

                # set bit at p2 position
                num = num | shift2

            # if bit at p2 position is set
            else:

                # set bit at p2 position
                num = num & (~shift2)

                # unset bit at p2 position
                num = num | shift1
        p1 += 1
        p2 += 1
        n -= 1

    # return final result
    return num


# Driver code
res = swapBits(28, 0, 3, 2)
print("Result =", res)

# This code is contributed by avanitrachhadiya2155
