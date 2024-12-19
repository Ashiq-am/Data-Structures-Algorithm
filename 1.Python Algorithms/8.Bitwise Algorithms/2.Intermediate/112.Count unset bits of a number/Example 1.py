# Python 3 program to count unset
# bits in an integer

def countunsetbits(n):
    count = 0

    # x holds one set digit at a time
    # starting from LSB to MSB of n.
    x = 1
    while (x < n + 1):
        if ((x & n) == 0):
            count += 1
        x = x << 1

    return count


# Driver code
if __name__ == '__main__':
    n = 17
    print(countunsetbits(n))

# This code is contributed by
# Shashank_Sharma
