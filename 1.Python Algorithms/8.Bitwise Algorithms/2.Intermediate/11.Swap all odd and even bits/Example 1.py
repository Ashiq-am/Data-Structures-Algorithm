# Python program to swap even and
# odd bits of a given number

# Function to swap even
# and odd bits
def swapBits(x):
    # Get all even bits of x
    even_bits = x & 0xAAAAAAAA

    # Get all odd bits of x
    odd_bits = x & 0x55555555

    # Right shift even bits
    even_bits >>= 1

    # Left shift odd bits
    odd_bits <<= 1
    for i in range(0, 32, 2):
        i_bit = (x >> 1) & 1  # find i th bit
        i_1_bit = (x >> (i + 1)) & 1  # find i+1 th bit

        # remove i_bit
        # remove i+1 th bit
        # put i_bit at i+1 location
        # put i+1 bit at i location

        x = x - (i_bit << i)  - \
            (i_1_bit << (i + 2))  + \
            (i_bit << (i + 1))  + \
            (i_1_bit << i)



    # Combine even and odd bits
    return (even_bits | odd_bits)


# Driver code
if __name__ == '__main__':
    x = 23  # 00010111

    # Output is 43 (00101011)
    print(swapBits(x))

# This code is contributed by Rajput-Ji
