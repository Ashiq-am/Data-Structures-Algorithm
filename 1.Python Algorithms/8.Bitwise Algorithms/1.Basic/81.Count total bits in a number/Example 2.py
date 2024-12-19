# Function to get no of bits
# in binary representation
# of positive integer

def countBits(n):
    count = 0
    while (n):
        count += 1
        n >>= 1

    return count


# Driver program
i = 65
print(countBits(i))

# This code is contributed
# by Smitha
