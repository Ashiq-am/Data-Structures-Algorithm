# Python3 program to change least bits to
# get desired OR value

# Returns count of bits in N
def bitCount(N):
    cnt = 0;
    while (N > 0):
        cnt += 1
        N >>= 1

    return cnt


# Returns bit at 'pos' position
def at_position(num, pos):
    bit = num & (1 << pos)
    return (bit != 0)


# Utility method to toggle bit at
# 'pos' position
def toggle(num, pos):
    num ^= (1 << pos)
    return num


# method returns minimum number of bit flip
# to get T as OR value of A and B
def minChangeToReachTaregetOR(A, B, K, T):
    maxlen = max(bitCount(A), bitCount(B), bitCount(T));

    # Loop over maximum number of bits among
    # A, B and T
    for i in range(maxlen - 1, -1, -1):

        bitA = at_position(A, i);
        bitB = at_position(B, i);
        bitT = at_position(T, i);

        # T's bit is set, try to toggle bit
        # of B, if not already
        if (bitT > 0):
            if ((not bitA) and (not bitB)):
                B = toggle(B, i)
                K -= 1

        else:
            # if A's bit is set, flip that
            if (bitA > 0):
                A = toggle(A, i)
                K -= 1

            # if B's bit is set, flip that
            if (bitB > 0):
                B = toggle(B, i)
                K -= 1

    # if K is less than 0 then we can make A|B == T
    if (K < 0):
        print("Not possible");
        return;

    # Loop over bits one more time to minimise
    # A further
    i = maxlen - 1
    while True:
        if K < 0 or i < 0:
            break

        bitA = at_position(A, i);
        bitB = at_position(B, i);
        bitT = at_position(T, i);

        if (bitT > 0):
            # If both bit are set, then Unset
            # A's bit to minimise it
            if (bitA and bitB):
                A = toggle(A, i)
                K -= 1

        # If A's bit is 1 and B's bit is 0,
        # toggle both
        if ((bitA != 0) and (not bitB) and K >= 2):
            A = toggle(A, i)
            B = toggle(B, i)
            K -= 2

        i -= 1

    # Output changed value of A and B
    print(A, B)


# Driver code
A = 175
B = 66
K = 5
T = 100
minChangeToReachTaregetOR(A, B, K, T)

# This code is contributed by phasing17
