def Add(x, y):

    if (y == 0):
        return x

    else:
        return Add(x ^ y, (x & y) << 1)

# This code is contributed by subhammahato348
