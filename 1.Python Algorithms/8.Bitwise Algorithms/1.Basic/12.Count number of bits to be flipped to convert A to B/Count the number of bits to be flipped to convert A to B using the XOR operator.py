# Python3 program for the above approach

# Function that count set bits


def countSetBits(n):

    count = 0
    while n:
        count += 1
        n &= (n-1)

    return count


# Function that return count of
# flipped number

def FlippedCount(a, b):
    # Return count of set bits in
    # a XOR b
    return countSetBits(a ^ b)

# Driver code
if __name__ == "__main__":
    a = 10
    b = 20

    # Function call
    print(FlippedCount(a, b))

# This code is contributed by "Sharad_Bhardwaj".
