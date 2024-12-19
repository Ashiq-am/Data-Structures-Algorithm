# Python3 program to find min operation to convert a to

# function to return min operation
def minOp(a1, b1):
    a1 = bin(a1)[2::].zfill(32)
    b1 = bin(b1)[2::].zfill(32)
    # if a1 == b1 return 0
    if (a1 == b1):
        return 0
    # if all bits of a = 0
    if (int(a1) == 0):
        return -1
    # if all bits of a =1
    # first convert a1 to int and then call a1 & a1+1
    if (int(a1) & (int(a1) + 1)) == 0:
        return -1

    # convert a and b to binary string

    # check where ai and bi are different
    # and count n where ai = 1 and m where ai = 0
    n = 0
    m = 0
    for i in range(len(b1)):
        if b1[i] != a1[i]:
            if a1[i] == '1':
                n += 1
            else:
                m += 1

    # return result
    return max(n, m)


# Driver program
a = 14
b = 1
print(minOp(a, b))

# This code is contributed by phasing17
