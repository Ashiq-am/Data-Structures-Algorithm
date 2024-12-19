# Python program to do recursive addition
# of two integers

def add(x, y):
    keep = (x & y) << 1;
    res = x ^ y;

    # If bitwise & is 0, then there
    # is not going to be any carry.
    # Hence result of XOR is addition.
    if (keep == 0):
        return res;

    return add(keep, res);


# Driver code

print(add(15, 38));

# This code is contributed by Princi Singh
