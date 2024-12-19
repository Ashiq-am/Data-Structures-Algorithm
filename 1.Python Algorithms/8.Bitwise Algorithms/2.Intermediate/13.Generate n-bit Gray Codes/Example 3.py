# Python3 implementation of the above approach
def GreyCode(n):
    # power of 2
    for i in range(1 << n):
        # Generating the decimal
        # values of gray code then using
        # bitset to convert them to binary form
        val = (i ^ (i >> 1))

        # Converting to binary string
        s = bin(val)[2::]
        print(s.zfill(n), end=" ")


# Driver Code
n = 4

# Function call
GreyCode(n)

# This code is contributed by phasing17
