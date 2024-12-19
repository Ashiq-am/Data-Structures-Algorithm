# Efficient Python 3
# program to set all even
# bits of a number

# return msb set number
def getmsb(n):
    # set all bits
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16

    # return msb
    # increment n by 1
    # and shift by 1
    return (n + 1) >> 1


# return even seted number
def getevenbits(n):
    # get msb here
    n = getmsb(n)

    # generate even bits like 101010..
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16

    # if bits is odd then shift by 1
    if (n & 1):
        n = n >> 1

    # return even set bits number
    return n


# set all even bits here
def setallevenbits(n):
    # take or with even set bits number
    return n | getevenbits(n)


n = 10
print(setallevenbits(n))

# This code is contributed by
# Smitha Dinesh Semwal
