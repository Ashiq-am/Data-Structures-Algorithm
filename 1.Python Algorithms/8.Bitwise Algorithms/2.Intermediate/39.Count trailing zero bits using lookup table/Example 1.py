# Python 3 code for counting trailing zeros
# in binary representation of a number
def countTrailingZero(x):
    count = 0
    while ((x & 1) == 0):
        x = x >> 1
        count += 1

    return count


# Driver Code
if __name__ == '__main__':
    print(countTrailingZero(11))

# This code is contributed by
# Sanjit_Prasad
