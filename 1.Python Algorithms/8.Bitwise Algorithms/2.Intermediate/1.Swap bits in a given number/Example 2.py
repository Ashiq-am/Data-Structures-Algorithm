# Python code to implement the approach
def swapBits(x, p1, p2, n):
    # xor contains xor of two sets
    xor = (((x >> p1) ^ (x >> p2)) & ((1 << n) - 1))

    # To swap two sets, we need to again XOR the xor with original sets
    return x ^ ((xor << p1) | (xor << p2))

# This code is contributed by sanjoy_62.
