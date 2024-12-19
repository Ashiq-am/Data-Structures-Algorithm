# Python code to demonstrate
# modulus division by power of 2


# This function will
# return n % d.
# d must be one of:
# 1, 2, 4, 8, 16, 32, …
def getModulo(n, d):
    return (n & (d - 1))


# Driver program to
# test above function
n = 6

# d must be a power of 2
d = 4
print(n, "modulo", d, "is",
      getModulo(n, d))

# This code is contributed by
# Smitha Dinesh Semwal
