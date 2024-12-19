# Python 3 program to find solution of Josephus
# problem when size of step is 2.


# Returns position of survivor among a circle
# of n persons and every second person being
# killed
def josephus(n):
    # An interesting observation is that
    # for every number of power of two
    # answer is 1 always.
    if (~(n & (n - 1)) and n):
        return 1

    # The trick is just to right rotate the
    # binary representation of n once.
    # Find whether the number shed off
    # during left shift is set or not

    Arr = list(map(lambda x: int(x), list(bin(n)[2:])))
    Arr = [0] * (64 - len(Arr)) + Arr

    # shifting the bitset Arr
    # f will become true once leftmost
    # set bit is found
    f = False
    for i in range(63, -1, -1):
        if (Arr[i] == 1 and not f):
            f = True
            Arr[i] = Arr[i - 1]

        if (f):
            # shifting bits
            Arr[i] = Arr[i - 1]

    Arr[0] = 1

    # changing bitset to int
    res = int(''.join(Arr), 2)
    return res


# Driver Program to test above function
if __name__ == '__main__':
    n = 16
    print("The chosen place is", josephus(n))
