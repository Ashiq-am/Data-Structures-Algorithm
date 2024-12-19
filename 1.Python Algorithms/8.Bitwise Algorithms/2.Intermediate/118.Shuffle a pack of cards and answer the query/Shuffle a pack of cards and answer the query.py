# Python3 program to find the card
# at given index after N shuffles

# Function to find card at given index
def shuffle(N, key):
    # Answer will be reversal
    # of N bits from MSB
    NO_OF_BITS = N
    reverse_num = 0

    # Calculating the reverse binary representation
    for i in range(NO_OF_BITS):
        temp = (key & (1 << i))
        if (temp):
            reverse_num |= (1 << ((NO_OF_BITS - 1) - i))

    # Printing the result
    print(reverse_num)


# Driver code

# No. of Shuffle Steps
N = 3

# Key position
key = 3
shuffle(N, key)

# This code is contributed by Anant Agarwal.
