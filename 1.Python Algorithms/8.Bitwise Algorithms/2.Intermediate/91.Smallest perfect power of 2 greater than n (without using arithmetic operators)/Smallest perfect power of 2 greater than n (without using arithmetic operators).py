# Python3 implementation of smallest
# perfect power of 2 greater than n

# Function to find smallest perfect
# power of 2 greater than n
def perfectPowerOf2(n):
    # To store perfect power of 2
    per_pow = 1

    while n > 0:
        # bitwise left shift by 1
        per_pow = per_pow << 1

        # bitwise right shift by 1
        n = n >> 1

    # Required perfect power of 2
    return per_pow


# Driver program to test above
n = 128
print("Perfect power of 2 greater than",
      n, ":", perfectPowerOf2(n))

# This code is contributed by "Sharad_Bhardwaj".
