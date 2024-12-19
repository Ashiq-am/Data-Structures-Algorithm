# Python3 program to count set bits by pre-storing
# count set bits in nibbles.

num_to_bits = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4];


# Recursively get nibble of a given number
# and map them in the array
def countSetBitsRec(num):
    nibble = 0;
    if (0 == num):
        return num_to_bits[0];

    # Find last nibble
    nibble = num & 0xf;

    # Use pre-stored values to find count
    # in last nibble plus recursively add
    # remaining nibbles.

    return num_to_bits[nibble] + countSetBitsRec(num >> 4);


# Driver code

num = 31;
print(countSetBitsRec(num));

# this code is contributed by mits
