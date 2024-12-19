# Python3 program to modify a bit at position
# p in n to b.

# Returns modified n.
def modifyBit(n, p, b):
    mask = 1 << p
    return (n & ~mask) | ((b << p) & mask)


# Driver code
def main():
    print(modifyBit(6, 2, 0))
    print(modifyBit(6, 5, 1))


if __name__ == '__main__':
    main()
# This code is contributed by PrinciRaj1992
