# Python3 program to find 1's complement of n.
def onesComplement(n):
    v = []

    # convert to binary representation
    while (n != 0):
        v.append(n % 2)
        n = n // 2

    v.reverse()

    # change 1's to 0 and 0's to 1
    for i in range(len(v)):
        if (v[i] == 0):
            v[i] = 1
        else:
            v[i] = 0

    # convert back to number representation
    two = 1
    for i in range(len(v) - 1, -1, -1):
        n = n + v[i] * two
        two = two * 2

    return n


# Driver code
n = 22

# Function call
print(onesComplement(n))

# This code is contributed by phasing17
