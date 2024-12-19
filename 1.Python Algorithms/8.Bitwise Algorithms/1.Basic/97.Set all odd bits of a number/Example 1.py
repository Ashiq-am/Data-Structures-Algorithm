''' Python3 code Set all odd bits
of a number'''


# set all odd bit
def oddbitsetnumber(n):
    count = 0
    # res for store 010101.. number
    res = 0

    # generate number form of 010101.....till
    # temp size
    temp = n
    while temp > 0:

        # if bit is odd, then generate
        # number and or with res
        if count % 2 == 0:
            res |= (1 << count)

        count += 1
        temp >>= 1

    return (n | res)


n = 10
print(oddbitsetnumber(n))

# This code is contributed by Shreyanshi Arun.
