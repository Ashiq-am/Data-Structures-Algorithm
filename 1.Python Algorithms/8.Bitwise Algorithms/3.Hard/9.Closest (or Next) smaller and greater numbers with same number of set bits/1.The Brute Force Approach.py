# Python 3 implementation of getNext with
# same number of bits 1's is below

# Main Function to find next smallest
# number bigger than n
def getNext(n):
    # Compute c0 and c1
    c = n
    c0 = 0
    c1 = 0

    while (((c & 1) == 0) and (c != 0)):
        c0 += 1
        c >>= 1

    while ((c & 1) == 1):
        c1 += 1
        c >>= 1

    # If there is no bigger number with
    # the same no. of 1's
    if (c0 + c1 == 31 or c0 + c1 == 0):
        return -1

    # position of rightmost non-trailing zero
    p = c0 + c1

    # Flip rightmost non-trailing zero
    n |= (1 << p)

    # Clear all bits to the right of p
    n &= ~((1 << p) - 1)

    # Insert (c1-1) ones on the right.
    n |= (1 << (c1 - 1)) - 1

    return n


# Driver Code
if __name__ == "__main__":
    n = 5  # input 1
    print(getNext(n))

    n = 8  # input 2
    print(getNext(n))

# This code is contributed by ita_c
