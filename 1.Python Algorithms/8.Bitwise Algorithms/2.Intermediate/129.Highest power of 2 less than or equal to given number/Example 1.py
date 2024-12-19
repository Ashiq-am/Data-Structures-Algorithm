# Python3 program to find highest
# power of 2 smaller than or
# equal to n.
def highestPowerof2(n):
    res = 0
    for i in range(n, 0, -1):

        # If i is a power of 2
        if ((i & (i - 1)) == 0):
            res = i
            break

    return res


# Driver code
n = 10
print(highestPowerof2(n))

# This code is contributed by mits
