# Python 3 program to find maximum number
# by swapping extreme bits.

def findMax(num):
    num_copy = num

    # Traverse bits from both extremes
    j = 4 * 8 - 1;
    i = 0
    while (i < j):

        # Obtaining i-th and j-th bits
        m = (num_copy >> i) & 1
        n = (num_copy >> j) & 1

        # Swapping the bits if lesser significant
        # is greater than higher significant
        # bit and accordingly modifying the number
        if (m > n):
            x = (1 << i | 1 << j)
            num = num ^ x

        i += 1
        j -= 1
    return num


# Driver code
if __name__ == "__main__":
    num = 4
    print(findMax(num))

# This code is contributed by ita_c
