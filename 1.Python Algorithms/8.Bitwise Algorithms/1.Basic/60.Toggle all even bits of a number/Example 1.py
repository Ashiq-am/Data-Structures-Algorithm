# Python code to Toggle all
# even bit of a number

# Returns a number which has all even
# bits of n toggled.
def evenbittogglenumber(n):
    # Generate number form of 101010
    # ..till of same order as n
    res = 0
    count = 0
    temp = n

    while (temp > 0):

        # if bit is even then generate
        # number and or with res
        if (count % 2 == 1):
            res = res | (1 << count)

        count = count + 1
        temp >>= 1

    # return toggled number
    return n ^ res


# Driver code
n = 11
print(evenbittogglenumber(n))

# This code is contributed by Nikita Tiwari.
