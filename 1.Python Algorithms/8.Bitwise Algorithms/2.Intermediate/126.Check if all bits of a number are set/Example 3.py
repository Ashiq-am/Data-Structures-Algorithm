def bitCount(n):
    n = n - ((n >> 1) & 0x55555555);
    n = (n & 0x33333333) + ((n >> 2) & 0x33333333);
    return ((n + (n >> 4) & 0xF0F0F0F) * 0x1010101) >> 24;


def isBitSet(N):
    if (N == pow(2, bitCount(N)) - 1):
        print("Yes");
    else:
        print("No");


if __name__ == '__main__':
    N = 7;
    isBitSet(N);

# This code is contributed by gauravrajput1
