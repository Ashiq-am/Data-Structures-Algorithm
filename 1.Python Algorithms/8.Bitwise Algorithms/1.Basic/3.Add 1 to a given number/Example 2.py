# Python3 code to add
# one to a given number
def addOne(x):
    m = 1;
    # Flip all the set bits
    # until we find a 0
    while (x & m):
        x = x ^ m
        m <<= 1

    # flip the rightmost
    # 0 bit
    x = x ^ m
    return x


# Driver program
n = 13
print(addOne(n))

# This code is contributed by Prerna Saini.
