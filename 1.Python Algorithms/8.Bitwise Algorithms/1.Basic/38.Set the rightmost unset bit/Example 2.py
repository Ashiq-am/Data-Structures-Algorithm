def setMostRightUnset(a):
    # Will get a number with all set
    # bits except the first set bit
    x = a ^ (a - 1)
    print(bin(x)[2:])

    # We reduce it to the number with
    # single 1's on the position of
    # first set bit in given number
    x = x & a
    print(bin(x)[2:])

    # Move x on right by one shift to
    # make OR operation and make first
    # rightest unset bit 1
    x = x >> 1

    b = a | x

    print("before setting bit ", bin(a)[2:])
    print("after setting bit ", bin(b)[2:])


# Driver Code
if __name__ == '__main__':
    a = 21

    setMostRightUnset(a)

# This code is contributed by mohit kumar 29
