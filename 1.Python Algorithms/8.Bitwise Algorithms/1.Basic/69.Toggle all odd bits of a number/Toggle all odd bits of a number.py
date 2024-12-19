# Python3 code for Toggle all odd bit of a number

# Returns a number which has all odd
# bits of n toggled.
def evenbittogglenumber(n):
    # Generate number form of 101010...
    # ..till of same order as n
    res = 0;
    count = 0;
    temp = n

    while (temp > 0):

        # If bit is odd, then generate
        # number and or with res
        if (count % 2 == 0):
            res = res | (1 << count)

        count = count + 1
        temp >>= 1

    # Return toggled number
    return n ^ res


# Driver code
if __name__ == '__main__':
    n = 11
    print(evenbittogglenumber(n))

# This code is contributed by Nikita Tiwari.
